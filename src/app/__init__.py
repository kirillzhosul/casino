# Casino App Module.

# Importing.

# Flask core.
from flask import Flask
from flask_restful import Api

# Type hints.
from typing import Optional, NoReturn


def create(name: Optional[str] = None) -> Flask:
    """
    Creates a new instance of app.
    :param name: __name__ for Flask constructor.
    :return: Flask app instance.
    """

    def _register_blueprints(_app: Flask, _api: Api) -> NoReturn:
        """
        Registers blueprints.
        :param _app: App (Can be ommitted).
        :param _api: Flask RESTful API (Can be ommitted).
        """

        # Importing views.
        from . import views

        # Registering.
        views.register_blueprints(_app, _api)

    # Process name parameter.
    name = name if name else __name__

    # Create app.
    app = Flask(name)

    # Create API.
    api = Api(app)

    # Configure.

    # Blueprints.
    _register_blueprints(app, api)

    # Return app instance.
    return app
