from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.extensions import db
from app.models.system import System
from app.utils.decorators import require_permission
from app.utils.audit import log_action
from app.utils.system_status import update_system_status

bp = Blueprint("systems", __name__, url_prefix="/systems")


@bp.route("/")
@login_required
def list_systems():
    systems = System.query.all()
    return render_template("systems/list.html", systems=systems)


@bp.route("/new", methods=["GET", "POST"])
@require_permission("edit_systems")
def create_system():
    if request.method == "POST":
        system = System(
            name=request.form["name"],
            description=request.form.get("description"),
            environment=request.form["environment"],
            system_type=request.form["system_type"],
            owner_team=request.form.get("owner_team"),
            owner_contact=request.form.get("owner_contact")
        )

        db.session.add(system)
        db.session.commit()

        log_action("CREATE_SYSTEM", "System", system.id)
        return redirect(url_for("systems.list_systems"))

    return render_template("systems/new.html")


@bp.route("/<int:system_id>/status", methods=["POST"])
@require_permission("edit_systems")
def change_status(system_id):
    system = System.query.get_or_404(system_id)
    new_status = request.form["status"]
    reason = request.form.get("reason")

    update_system_status(system, new_status, current_user.id, reason)
    log_action("CHANGE_SYSTEM_STATUS", "System", system.id)

    return redirect(url_for("systems.list_systems"))
