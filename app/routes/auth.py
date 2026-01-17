from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    return render_template("login.html")


@bp.route("/logout")
def logout():
    return redirect(url_for("auth.login"))
