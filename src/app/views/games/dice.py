# Casino App Dice Game Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, render_template


# Blueprint.
bp_game_dice = Blueprint(name="game_dice", import_name=__name__, url_prefix="/games/dice/")


@bp_game_dice.route("/", methods=["GET"])
def index() -> str:
    """
    Dice game index page route.
    :return: Page.
    """

    # Returning response.
    return render_template("/games/dice/dice.index.html.jinja")
