# Casino App Root Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, render_template
from flask_login import current_user

# Blueprint.
bp_root = Blueprint(name="root", import_name=__name__, url_prefix="/")


@bp_root.route("/", methods=["GET"])
def index() -> str:
    """
    Root index page route.
    :return: Page.
    """

    # Returning response.
    return render_template("/root/root.index.html.jinja",
                           current_user=current_user)
