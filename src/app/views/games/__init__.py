# Casino App Games Views (Blueprints).

# Importing.

# Flask class.
from flask import Flask

# Type hints.
from typing import NoReturn


def register_blueprints(app: Flask) -> NoReturn:
    """
    Registers blueprints for given application.
    :param app: Flask app.
    """

    # Importing views blueprints.
    from .dice import bp_game_dice

    # Registering views blueprints.
    app.register_blueprint(bp_game_dice)

