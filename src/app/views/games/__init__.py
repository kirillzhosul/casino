# Casino App Games Views (Blueprints).

# Importing.

# Flask.
from flask import Flask
from flask_restful import Api

# Type hints.
from typing import NoReturn


def register_blueprints(app: Flask, api: Api) -> NoReturn:
    """
    Registers blueprints for given application.
    :param app: Flask app.
    :param api: Flask RESTful API.
    """

    # Importing views blueprints.
    from .games import bp_games

    # Registering views blueprints.
    app.register_blueprint(bp_games)
