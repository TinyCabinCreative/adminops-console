from flask import request
from flask_login import current_user
from app.extensions import db
from app.models.audit_log import AuditLog

def log_action(action, resource_type, resource_id=None):
    log = AuditLog(
        user_id=current_user.id if current_user.is_authenticated else None,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        ip_address=request.remote_addr,
        user_agent=request.headers.get("User-Agent")
    )
    db.session.add(log)
    db.session.commit()
