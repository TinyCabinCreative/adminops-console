from datetime import datetime
from app.extensions import db

class SystemStatusLog(db.Model):
    __tablename__ = "system_status_logs"

    id = db.Column(db.Integer, primary_key=True)

    system_id = db.Column(db.Integer, db.ForeignKey("systems.id"))
    system = db.relationship("System", backref="status_logs")

    old_status = db.Column(db.String(30))
    new_status = db.Column(db.String(30))

    reason = db.Column(db.Text, nullable=True)

    changed_at = db.Column(db.DateTime, default=datetime.utcnow)
    changed_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))
