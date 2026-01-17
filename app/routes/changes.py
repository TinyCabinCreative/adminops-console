from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.extensions import db
from app.models.change_record import ChangeRecord
from app.models.system import System
from app.utils.decorators import require_permission
from app.utils.audit import log_action
from app.utils.change_status import update_change_status

bp = Blueprint("changes", __name__, url_prefix="/changes")


@bp.route("/")
@login_required
def list_changes():
    changes = ChangeRecord.query.order_by(ChangeRecord.created_at.desc()).all()
    return render_template("changes/list.html", changes=changes)


@bp.route("/new", methods=["GET", "POST"])
@require_permission("approve_changes")
def create_change():
    systems = System.query.all()

    if request.method == "POST":
        change = ChangeRecord(
            title=request.form["title"],
            description=request.form["description"],
            change_type=request.form["change_type"],
            risk_level=request.form["risk_level"],
            emergency=bool(request.form.get("emergency")),
            system_id=request.form["system_id"],
            created_by_id=current_user.id
        )

        db.session.add(change)
        db.session.commit()

        log_action("CREATE_CHANGE", "ChangeRecord", change.id)
        return redirect(url_for("changes.list_changes"))

    return render_template("changes/new.html", systems=systems)


@bp.route("/<int:change_id>/status", methods=["POST"])
@require_permission("approve_changes")
def update_status(change_id):
    change = ChangeRecord.query.get_or_404(change_id)
    new_status = request.form["status"]

    update_change_status(change, new_status, current_user.id)
    log_action("UPDATE_CHANGE_STATUS", "ChangeRecord", change.id)

    return redirect(url_for("changes.list_changes"))
