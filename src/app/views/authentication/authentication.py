"""
Casino App Authentication Views (Blueprint).
"""

# Importing.

# Flask.
from flask import Blueprint, Response, render_template, request, jsonify
from flask_login import current_user
from flask_restful import reqparse

# Typing.
from typing import Union, Tuple

# Blueprint.
bp_authentication = Blueprint(name="authentication", import_name=__name__, url_prefix="/authentication/")

# Signup argument parser.
signup_parser = reqparse.RequestParser()
signup_parser.add_argument("username", type=str)
signup_parser.add_argument("email", type=str)
signup_parser.add_argument("password", type=str)
signup_parser.add_argument("password_confirmation", type=str)

# Login argument parser.
login_parser = reqparse.RequestParser()


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

        # Parsing arguments.
        arguments = signup_parser.parse_args(request)

        # Arguments.
        signup_username = arguments.get("username")
        signup_email = arguments.get("email")
        signup_password = arguments.get("password")
        signup_password_confirmation = arguments.get("password_confirmation")

        if signup_username is None or signup_email is None or signup_password is None or signup_password_confirmation is None:
            # If one of the arguemnts is not passed.

            # Error.
            return jsonify({
                "error": "Invalid request arguments! "
                         "`username`, `email` or `password` or `password_confirmation` is not passed!"
            }), 400

        if signup_password != signup_password_confirmation:
            # Not same passwords.

            # Error.
            return jsonify({
                "error": "Password and its confirmation do not match!"
            }), 400

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
