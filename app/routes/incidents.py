from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.extensions import db
from app.models.incident import Incident
from app.models.incident_update import IncidentUpdate
from app.models.system import System
from app.utils.decorators import require_permission
from app.utils.audit import log_action

bp = Blueprint("incidents", __name__, url_prefix="/incidents")


@bp.route("/")
@login_required
def list_incidents():
    incidents = Incident.query.order_by(Incident.created_at.desc()).all()
    return render_template("incidents/list.html", incidents=incidents)


@bp.route("/new", methods=["GET", "POST"])
@require_permission("create_incidents")
def create_incident():
    systems = System.query.all()

    if request.method == "POST":
        incident = Incident(
            title=request.form["title"],
            description=request.form["description"],
            severity=request.form["severity"],
            system_id=request.form.get("system_id") or None,
            created_by_id=current_user.id
        )

        db.session.add(incident)
        db.session.commit()

        log_action("CREATE_INCIDENT", "Incident", incident.id)
        return redirect(url_for("incidents.view_incident", incident_id=incident.id))

    return render_template("incidents/new.html", systems=systems)


@bp.route("/<int:incident_id>", methods=["GET", "POST"])
@login_required
def view_incident(incident_id):
    incident = Incident.query.get_or_404(incident_id)

    if request.method == "POST":
        update = IncidentUpdate(
            incident_id=incident.id,
            message=request.form["message"],
            status_change=request.form.get("status"),
            created_by_id=current_user.id
        )

        if update.status_change:
            incident.status = update.status_change

        db.session.add(update)
        db.session.commit()

        log_action("UPDATE_INCIDENT", "Incident", incident.id)
        return redirect(url_for("incidents.view_incident", incident_id=incident.id))

    return render_template("incidents/view.html", incident=incident)
