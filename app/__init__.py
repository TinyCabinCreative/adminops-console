from flask import Flask
from .extensions import db, login_manager
from .routes import auth, dashboard, users, systems, incidents, changes, audit

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(systems.bp)
    app.register_blueprint(incidents.bp)
    app.register_blueprint(changes.bp)
    app.register_blueprint(audit.bp)

    return app
