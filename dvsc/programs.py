import os

from flask import Blueprint, flash, send_from_directory, session
from flask import render_template
from flask import request
from flask import session
from flask import redirect, url_for
from .auth import login_required
from .config import PROGRAMS, TOKEN

bp = Blueprint("downloads", __name__)


@bp.route("/")
@login_required
def index():
    """Show all the posts, most recent first."""
    return render_template("programs/index.jinja", downloads=PROGRAMS)


@bp.route("/<int:id>")
@login_required
def download(id):
    if "locked" in PROGRAMS[id]:
        if "valid_token" not in session or session["valid_token"] != TOKEN:
            return redirect(url_for("downloads.unlock"))

    return send_from_directory(
        os.path.join("programs"),
        PROGRAMS[id]["filename"]
    )


@bp.route("/unlock", methods=("GET", "POST"))
@login_required
def unlock():
    if request.method == "POST":
        token = request.form["token"]

        if token == TOKEN:
            session["valid_token"] = token
            return redirect(url_for("index"))
        else:
            flash("Invalid token!", "error")
    
    return render_template("programs/locked.jinja")

