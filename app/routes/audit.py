from flask import Blueprint, render_template, request
from app.models.audit_log import AuditLog
from app.utils.decorators import require_permission

bp = Blueprint("audit", __name__, url_prefix="/audit")

@bp.route("/")
@require_permission("view_audit_logs")
def audit_logs():
    query = AuditLog.query

    action = request.args.get("action")
    user_id = request.args.get("user_id")
    resource = request.args.get("resource_type")

    if action:
        query = query.filter_by(action=action)
    if user_id:
        query = query.filter_by(user_id=user_id)
    if resource:
        query = query.filter_by(resource_type=resource)

    logs = query.order_by(AuditLog.timestamp.desc()).limit(500).all()
    return render_template("audit/logs.html", logs=logs)
