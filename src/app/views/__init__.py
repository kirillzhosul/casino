# Casino App Views (Blueprints).

# Importing.

# Flask class.
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

    # Importing submodules to register their blueprints.
    from . import games

    # Importing views blueprints.
    from .root import bp_root

    # Registering views blueprints.
    app.register_blueprint(bp_root)

    # Registering submodules blueprints.
    games.register_blueprints(app, api)
