from datetime import datetime
from app.extensions import db

class ChangeRecord(db.Model):
    __tablename__ = "change_records"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

    change_type = db.Column(db.String(50), nullable=False)
    # config / deployment / patch / access / emergency

    status = db.Column(db.String(30), default="DRAFT")

    risk_level = db.Column(db.String(20), nullable=False)
    # low / medium / high

    rollback_plan = db.Column(db.Text, nullable=True)

    emergency = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    implemented_at = db.Column(db.DateTime, nullable=True)

    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    approved_by_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    system_id = db.Column(db.Integer, db.ForeignKey("systems.id"))
    system = db.relationship("System", backref="changes")
