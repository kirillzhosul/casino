# Casino App Module.

# Importing.

# Flask core.
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Type hints.
from typing import Optional, NoReturn

# Default app fields.
database = SQLAlchemy()


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

    def _configure_config(_app: Flask) -> NoReturn:
        """ Confgures app. """

        # SQL Alchemy.
        _app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    def _configure_database(_app: Flask) -> NoReturn:
        pass

    # Process name parameter.
    name = name if name else __name__

    # Create app.
    app = Flask(name)

    # Create API.
    api = Api(app)

    # Initialise database application.
    database.init_app(app)

    # Configure.

    # Config.
    _configure_config(app)

    # Database.
    _configure_database(app)

    # Blueprints.
    _register_blueprints(app, api)

    # Return app instance.
    return app
