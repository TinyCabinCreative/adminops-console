from datetime import datetime
from app.extensions import db

class Incident(db.Model):
    __tablename__ = "incidents"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

    severity = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(30), default="OPEN")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_by = db.relationship("User")

    system_id = db.Column(db.Integer, db.ForeignKey("systems.id"), nullable=True)
