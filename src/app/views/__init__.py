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

    # Importing submodules to register their blueprints.
    from . import games
    from . import authentication

    # Importing views blueprints.
    from .root import bp_root

    # Registering views blueprints.
    app.register_blueprint(bp_root)

    # Registering submodules blueprints.
    games.register_blueprints(app)
    authentication.register_blueprints(app)
