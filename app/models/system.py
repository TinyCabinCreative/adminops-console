from datetime import datetime
from app.extensions import db

class System(db.Model):
    __tablename__ = "systems"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    environment = db.Column(db.String(20), nullable=False)  # prod / staging / dev
    system_type = db.Column(db.String(50), nullable=False)  # server / app / db / service

    status = db.Column(db.String(30), default="HEALTHY")  # HEALTHY / DEGRADED / OFFLINE

    owner_team = db.Column(db.String(100), nullable=True)
    owner_contact = db.Column(db.String(150), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
