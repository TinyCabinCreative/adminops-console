from flask import Blueprint, render_template
from flask_login import login_required
from app.models.audit_log import AuditLog
from app.utils.decorators import require_permission

bp = Blueprint("audit", __name__, url_prefix="/audit")


@bp.route("/")
@login_required
@require_permission("view_audit_logs")
def view_audit_logs():
    logs = AuditLog.query.order_by(AuditLog.timestamp.desc()).limit(200).all()
    return render_template("audit/logs.html", logs=logs)
