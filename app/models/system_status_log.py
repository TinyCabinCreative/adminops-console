from datetime import datetime
from app.extensions import db

class SystemStatusLog(db.Model):
    __tablename__ = "system_status_logs"

    id = db.Column(db.Integer, primary_key=True)
    system_id = db.Column(db.Integer, nullable=False)
    old_status = db.Column(db.String(50), nullable=False)
    new_status = db.Column(db.String(50), nullable=False)
    changed_at = db.Column(db.DateTime, default=datetime.utcnow)
