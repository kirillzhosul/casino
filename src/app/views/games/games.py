# Casino App Dice Game Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, Response, render_template, request, jsonify
from flask_restful import reqparse

# Random.
from random import randint

# Type hints.
from typing import Union, Tuple


# Blueprint.
bp_games = Blueprint(name="games", import_name=__name__, url_prefix="/games/")

# Dice argument parser.
dice_parser = reqparse.RequestParser()
dice_parser.add_argument("bet_size", type=int)
dice_parser.add_argument("bet_percent", type=int)
dice_parser.add_argument("bet_type", type=str)


@bp_games.route("/dice/", methods=["GET", "POST"])
def dice() -> Union[str, Response, Tuple[Response, int]]:
    """
    Dice game index page route.
    :return: Page.
    """

    if request.method == "POST":
        # If API request.

        # Get arguments
        arguments = dice_parser.parse_args(request)

        # Getting bet arguments.
        bet_size = arguments["bet_size"]
        bet_percent = arguments["bet_percent"]
        bet_type = arguments["bet_type"]

        if bet_size is None or bet_percent is None or bet_type is None:
            # If one of the arguemnts is not pased.

            # Error.
            return jsonify({
                "error": "Invalid request arguments! `bet_size`, `bet_percent` or `bet_type` is not passed!"
            }), 400

        if bet_percent < 1 or bet_percent > 95:
            # If invalid percentage.

            # Error.
            return jsonify({
                "error": "Invalid bet percent! `bet_percent` should be between 1 and 95."
            }), 400

        if bet_size < 1:
            # If invalid bet size.

            # Error.
            return jsonify({
                "error": "Invalid bet size! `bet_size` should be not less than 1."
            }), 400

        if bet_type == "min" or bet_type == "max":
            # If valid bet type.

            # Max range for the bet value.
            bet_value_range = 1_000_000

            # Difference for threshold max and min calculation.
            bet_required_threshold_difference = (bet_value_range / 100) * bet_percent

            # Getting max and minimim.
            if bet_type == "max":
                bet_required_threshold_max = bet_required_threshold_difference
                bet_required_threshold_min = 0
            else:  # elif bet_type == "min":
                bet_required_threshold_max = bet_value_range
                bet_required_threshold_min = bet_required_threshold_max - bet_required_threshold_difference

            # Get total win size.
            bet_win_size = (100 / bet_percent * bet_size)

            # Getting random bet value.
            bet_value = randint(0, bet_value_range)

            # Bet result (win or fail).
            bet_result = bet_required_threshold_min < bet_value < bet_required_threshold_max
        else:
            # Not found.

            # Error.
            return jsonify({
                "error": "Invalid bet type! `bet_type` should be `min` or `max`."
            }), 400

        # Returning response.
        return jsonify({
            "bet_arguments": {
                "bet_size": bet_size,
                "bet_percent": bet_percent,
                "bet_type": bet_type
            },
            "bet_response": {
                "bet_value": bet_value,
                "bet_win_size": bet_win_size,
                "bet_required_threshold": {
                    "min": bet_required_threshold_min,
                    "max": bet_required_threshold_max
                },
                "bet_result": bet_result
            },
        })

    # Returning response.
    return render_template("/games/dice/dice.index.html.jinja")
