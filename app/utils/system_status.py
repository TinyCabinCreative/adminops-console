from app.extensions import db
from app.models.system_status_log import SystemStatusLog

def update_system_status(system, new_status, user_id, reason=None):
    log = SystemStatusLog(
        system_id=system.id,
        old_status=system.status,
        new_status=new_status,
        reason=reason,
        changed_by_id=user_id
    )

    system.status = new_status
    db.session.add(log)
    db.session.commit()
