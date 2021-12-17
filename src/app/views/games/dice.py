# Casino App Dice Game Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, Response


# Blueprint.
bp_game_dice = Blueprint(name="game_dice", import_name=__name__, url_prefix="/games/dice/")


@bp_game_dice.route("/", methods=["GET"])
def game_dice_index() -> Response:
    """
    Dice game index page route.
    :return: Page.
    """

    # Returning response.
    return Response("Dice game!")
