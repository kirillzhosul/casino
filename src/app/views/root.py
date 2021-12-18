# Casino App Root Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, render_template


# Blueprint.
bp_root = Blueprint(name="root", import_name=__name__, url_prefix="/")


@bp_root.route("/", methods=["GET"])
def index() -> str:
    """
    Root index page route.
    :return: Page.
    """

    # Returning response.
    return render_template("/root/root.index.html.jinja")
