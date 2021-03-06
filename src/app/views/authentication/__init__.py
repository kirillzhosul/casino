"""
Casino App Games Views (Blueprints).
"""

# Importing.

# Flask.
from flask import Flask

# Type hints.
from typing import NoReturn


def register_blueprints(app: Flask) -> NoReturn:
    """
    Registers blueprints for given application.
    :param app: Flask app.
    """

    # Importing views blueprints.
    from .authentication import bp_authentication

    # Registering views blueprints.
    app.register_blueprint(bp_authentication)
