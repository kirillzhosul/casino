# Casino App Root Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, Response


# Blueprint.
bp_root = Blueprint(name="root", import_name=__name__, url_prefix="/")


@bp_root.route("/", methods=["GET"])
def root_index() -> Response:
    """
    Root index page route.
    :return: Page.
    """

    # Returning response.
    return Response("Casino Test Index Page. 200 OK!")
