from flask import Blueprint, render_template
from flask_login import login_required
from app.models.system import System
from app.models.incident import Incident
from app.models.change_record import ChangeRecord

bp = Blueprint("dashboard", __name__)

@bp.route("/")
@login_required
def dashboard():
    stats = {
        "systems_total": System.query.count(),
        "incidents_open": Incident.query.filter_by(status="OPEN").count(),
        "changes_pending": ChangeRecord.query.filter(
            ChangeRecord.status.in_(["DRAFT", "SUBMITTED"])
        ).count()
    }

    return render_template("dashboard.html", stats=stats)
