from flask import Blueprint, render_template

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/")
def index():
    demo_users = [
        {"id": 1, "username": "admin", "role": "Administrator"},
        {"id": 2, "username": "jvenne", "role": "Analyst"},
    ]

    return render_template("users.html", users=demo_users)
