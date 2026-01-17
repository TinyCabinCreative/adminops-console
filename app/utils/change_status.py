from datetime import datetime
from app.extensions import db
from app.models.change_status_log import ChangeStatusLog

def update_change_status(change, new_status, user_id, comment=None):
    log = ChangeStatusLog(
        change_id=change.id,
        old_status=change.status,
        new_status=new_status,
        comment=comment,
        changed_by_id=user_id
    )

    change.status = new_status
    if new_status == "IMPLEMENTED":
        change.implemented_at = datetime.utcnow()

    db.session.add(log)
    db.session.commit()
