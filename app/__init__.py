from flask import Flask, app
from .extensions import db, login_manager
from app.extensions import db
from werkzeug.security import generate_password_hash
from app.models.user import User
from .routes import auth, dashboard, users, systems, incidents, changes, audit

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
     db.create_all()
    with app.app_context():
     if not User.query.filter_by(username="admin").first():
        admin = User(
            username="admin",
            password_hash=generate_password_hash("admin123")
        )
        db.session.add(admin)
        db.session.commit()

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(systems.bp)
    app.register_blueprint(incidents.bp)
    app.register_blueprint(changes.bp)
    app.register_blueprint(audit.bp)

    return app

from app import models