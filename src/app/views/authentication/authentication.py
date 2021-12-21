# Casino App Authentication Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, render_template
from flask_login import current_user

# Blueprint.
bp_authentication = Blueprint(name="authentication", import_name=__name__, url_prefix="/authentication/")


@bp_authentication.route("/login", methods=["GET"])
def login() -> str:
    """
    Authentication login page route.
    :return: Page.
    """

    # Returning response.
    return render_template("/authentication/authentication.login.html.jinja",
                           current_user=current_user)


@bp_authentication.route("/signup", methods=["GET"])
def signup() -> str:
    """
    Authentication signup page route.
    :return: Page.
    """

    # Returning response.
    return render_template("/authentication/authentication.signup.html.jinja",
                           current_user=current_user)
