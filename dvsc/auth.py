import functools
import time

from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from dvsc.config import PASSWORD

bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if "is_authorized" not in session or session["is_authorized"] is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        password = request.form["password"]
        if "debug" in request.form:
            is_debug = True
        else:
            is_debug = False

        error = None
        is_good_pass = True

        if len(password) != len(PASSWORD):
            is_good_pass = False

        i = 0
        delay = 0
        while is_good_pass and i < len(PASSWORD):
                if password[i] != PASSWORD[i]:
                    is_good_pass = False
        
                # Enforce delay on attacker trying to bruteforce!
                time.sleep(0.15)
                delay += 150
                i += 1
    
        if not is_good_pass:
            error = "Incorrect password!"

        if error is None:
            session.clear()
            session["is_authorized"] = True
            return redirect(url_for("index"))

        if is_debug:
            error += f"\nPage generated in {delay} ms."

        flash(error)

    return render_template("auth/login.jinja")


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))
