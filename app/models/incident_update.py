from datetime import datetime
from app.extensions import db

class IncidentUpdate(db.Model):
    __tablename__ = "incident_updates"

    id = db.Column(db.Integer, primary_key=True)
    incident_id = db.Column(db.Integer, db.ForeignKey("incidents.id"))
    incident = db.relationship("Incident", backref="updates")

    message = db.Column(db.Text, nullable=False)
    status_change = db.Column(db.String(30), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))
