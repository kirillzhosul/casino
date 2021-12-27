# Casino App Dice Game Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, Response, render_template, request, jsonify
from flask_restful import reqparse
from flask_login import current_user

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

# Dice settings.

# Max range for the bet value.
DICE_BET_VALUE_RANGE = 1_000_000

# Chance to lose bet.
DICE_BET_CHEATING_LOSE_CHANCE = 0


class DiceBetResult(object):
    """ Dice game result container object. """

    def __init__(self, result: bool, win_size: float, value: int, required_threshold: Tuple[int, int]):
        # Constrcutor.

        # Fields.
        self.result = result
        self.win_size = win_size
        self.value = value
        self.required_threshold = required_threshold


def dice_calculate(bet_size: int, bet_percent: int, bet_type: str) -> DiceBetResult:
    """
    Calculates dice game
    :param bet_size: Amount.
    :param bet_percent: Percent.
    :param bet_type: `min` or `max`
    :return: DiceGameBetResult as result object container.
    """

    # Error check.
    assert bet_type in ("min", "max"), "Invalid argument!"

    # Difference for threshold max and min calculation.
    bet_required_threshold_difference = (DICE_BET_VALUE_RANGE / 100) * bet_percent

    # Getting random bet value.
    bet_value = randint(0, DICE_BET_VALUE_RANGE)

    # Get total win size.
    bet_win_size = float(format(100 / bet_percent * bet_size, ".2f"))

    # Getting max and minimim.
    if bet_type == "max":
        bet_required_threshold_max = bet_required_threshold_difference
        bet_required_threshold_min = 0
    else:
        bet_required_threshold_max = DICE_BET_VALUE_RANGE
        bet_required_threshold_min = bet_required_threshold_max - bet_required_threshold_difference

    if DICE_BET_CHEATING_LOSE_CHANCE != 0 and randint(0, 100) < DICE_BET_CHEATING_LOSE_CHANCE:
        # If chance to lose.

        # Recalculate with bet value not in given range.
        if bet_type == "max":
            bet_value = randint(bet_required_threshold_max, DICE_BET_VALUE_RANGE)
        else:
            bet_value = randint(0, int(bet_required_threshold_max - bet_required_threshold_difference))

    # Bet result (win or fail).
    bet_result = bet_required_threshold_min < bet_value < bet_required_threshold_max

    # Returning game result.
    return DiceBetResult(bet_result, bet_win_size, bet_value, (bet_required_threshold_min, bet_required_threshold_max))


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
        bet_size = arguments.get("bet_size")
        bet_percent = arguments.get("bet_percent")
        bet_type = arguments.get("bet_type")

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

        if not (bet_type == "min" or bet_type == "max"):
            # If not valid bet type.

            # Error.
            return jsonify({
                "error": "Invalid bet type! `bet_type` should be `min` or `max`."
            }), 400

        # Getting result.
        bet_result = dice_calculate(bet_size, bet_percent, bet_type)

        # Returning response.
        return jsonify({
            "bet_arguments": {
                "bet_size": bet_size,
                "bet_percent": bet_percent,
                "bet_type": bet_type
            },
            "bet_response": {
                "bet_value": bet_result.value,
                "bet_win_size": bet_result.win_size,
                "bet_required_threshold": {
                    "min": bet_result.required_threshold[0],
                    "max": bet_result.required_threshold[1]
                },
                "bet_result": bet_result.result
            },
        })

    # Returning response.
    return render_template("/games/dice/dice.index.html.jinja",
                           current_user=current_user)
