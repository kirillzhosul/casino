# Casino App Module.

# Importing.

# Flask core.
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Type hints.
from typing import Optional, NoReturn

# Database.
import os.path

# Default app fields.
db = SQLAlchemy()
login_manager = LoginManager()


def create(name: Optional[str] = None) -> Flask:
    """
    Creates a new instance of app.
    :param name: __name__ for Flask constructor.
    :return: Flask app instance.
    """

    def _register_blueprints(_app: Flask) -> NoReturn:
        """
        Registers blueprints.
        :param _app: App (Can be ommitted).
        """

        # Importing views.
        from . import views

        # Registering.
        views.register_blueprints(_app)

    def _configure_config(_app: Flask) -> NoReturn:
        """ Confgures app. """

        # Security.
        app.config["SECRET_KEY"] = "*FPHa(;LE]OKT,spwb>lHJ{J]dAs>%"

        # Database.
        _app.config["SQLALCHEMY_DATABASE_FILENAME"] = "database\\database.db"
        _app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        _app.config["SQLALCHEMY_DATABASE_URI"] = \
            f"sqlite:///" \
            f"{os.path.join(os.path.abspath(os.path.dirname(__file__)), _app.config['SQLALCHEMY_DATABASE_FILENAME'])}"

    def _configure_login_manager(_app: Flask) -> NoReturn:
        """ Configures login manager. """

        # Importing user database model.
        from .database.models.user import User

        # Initialise login manager.
        login_manager.init_app(_app)

        @login_manager.user_loader
        def _login_manager_load_user(user_id: int) -> Optional[User]:
            """
            Loads user from database.
            :param user_id: User id to load.
            :return: User or None
            """

            # Return.
            return User.query.get(int(user_id))

    def _configure_database(_app: Flask) -> NoReturn:
        """ Configures database. """

        # Importing models.
        from .database.models.user import User

        # Initialise database application.
        db.init_app(_app)

        # Path to the database.
        database_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                     _app.config["SQLALCHEMY_DATABASE_FILENAME"])

        if not os.path.exists(database_path):
            # If no database file.

            # Creating.
            db.create_all(app=_app)

    # Process name parameter.
    name = name if name else __name__

    # Create app.
    app = Flask(name)

    # Configure.

    # Config.
    _configure_config(app)

    # Database.
    _configure_database(app)

    # Login manager.
    _configure_login_manager(app)

    # Blueprints.
    _register_blueprints(app)

    # Return app instance.
    return app
