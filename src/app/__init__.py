# Casino App Module.

# Importing.

# Flask core.
from flask import Flask

# Type hints.
from typing import Optional


def create(name: Optional[str] = None) -> Flask:
    """
    Creates a new instance of app.
    :param name: __name__ for Flask constructor.
    :return: Flask app instance.
    """

    # Create app.
    name = name if name else __name__
    app = Flask(name)

    # Return app instance.
    return app
