from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

with app.app_context():
    if not User.query.filter_by(username="admin").first():
        user = User(username="admin")
        user.set_password("admin123")
        db.session.add(user)
        db.session.commit()
        print("Demo admin user created")
    else:
        print("Demo admin user already exists")
