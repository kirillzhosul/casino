# Casino App Module.

# Importing.

# Database object.
from ... import db


class User(db.Model):
    """ User database model that implements the User. """

    # Databse index.
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    # Username to login and identificate.
    username = db.Column(db.String, nullable=False)

    # Password to login.
    password = db.Column(db.String, nullable=False)
