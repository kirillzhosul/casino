# Casino App Dice Game Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, render_template


# Blueprint.
bp_games = Blueprint(name="games", import_name=__name__, url_prefix="/games/")


@bp_games.route("/dice/", methods=["GET"])
def dice() -> str:
    """
    Dice game index page route.
    :return: Page.
    """

    # Returning response.
    return render_template("/games/dice/dice.index.html.jinja")
