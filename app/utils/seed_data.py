from app.extensions import db
from app.models.system import System
from app.models.incident import Incident
from app.models.change_record import ChangeRecord

def seed_demo_data():
    web = System(
        name="Public Website",
        environment="prod",
        system_type="web",
        status="HEALTHY",
        owner_team="Platform"
    )

    api = System(
        name="Auth API",
        environment="prod",
        system_type="service",
        status="DEGRADED",
        owner_team="Security"
    )

    db.session.add_all([web, api])
    db.session.commit()

    incident = Incident(
        title="Login failures",
        description="Users unable to authenticate",
        severity="HIGH",
        status="OPEN",
        system_id=api.id
    )

    change = ChangeRecord(
        title="Rotate auth secrets",
        description="Emergency credential rotation",
        change_type="emergency",
        risk_level="high",
        emergency=True,
        system_id=api.id
    )

    db.session.add_all([incident, change])
    db.session.commit()
