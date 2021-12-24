# Casino App Authentication Views (Blueprint).

# Importing.

# Flask.
from flask import Blueprint, Response, render_template, request, jsonify
from flask_login import current_user

# Typing.
from typing import Union, Tuple

# Blueprint.
bp_authentication = Blueprint(name="authentication", import_name=__name__, url_prefix="/authentication/")


@bp_authentication.route("/login", methods=["GET", "POST"])
def login() -> Union[str, Response, Tuple[Response, int]]:
    """
    Authentication login page route.
    :return: Page.
    """

    if request.method == "POST":
        # If API request.

        # Boilerplate.
        return jsonify({
            "authentication": {
                "status": False,
                "message": "Not implemented yet."
            }
        })

    # Returning response.
    return render_template("/authentication/authentication.login.html.jinja",
                           current_user=current_user)


@bp_authentication.route("/signup", methods=["GET", "POST"])
def signup() -> Union[str, Response, Tuple[Response, int]]:
    """
    Authentication signup page route.
    :return: Page.
    """

    if request.method == "POST":
        # If API request.

        # Boilerplate.
        return jsonify({
            "authentication": {
                "status": False,
                "message": "Not implemented yet."
            }
        })

    # Returning response.
    return render_template("/authentication/authentication.signup.html.jinja",
                           current_user=current_user)
