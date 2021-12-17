# Casino App Views (Blueprints).

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
    from .root import bp_root

    # Registering views blueprints.
    app.register_blueprint(bp_root)
