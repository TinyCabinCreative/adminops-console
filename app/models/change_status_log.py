from datetime import datetime
from app.extensions import db

class ChangeStatusLog(db.Model):
    __tablename__ = "change_status_logs"

    id = db.Column(db.Integer, primary_key=True)
    change_id = db.Column(db.Integer, nullable=False)
    old_status = db.Column(db.String(50), nullable=False)
    new_status = db.Column(db.String(50), nullable=False)
    changed_at = db.Column(db.DateTime, default=datetime.utcnow)
