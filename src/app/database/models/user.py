# Casino App Module.

# Importing.

# Database object.
import password as password
import username as username

from ... import db


class User(db.Model):
    """ User database model that implements the User. """

    # Databse index.
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    # Username to login and identificate.
    username = db.Column(db.String, nullable=False)

    # Password to login.
    password = db.Column(db.String, nullable=False)

    # User balance.
    balance = db.Column(db.Integer, nullable=False)

    def __init__(self, password: str, username: str = "user"):
        """ Constructor. """

        # Login information.
        self.username = username
        self.password = password

        # Other.
        self.balance = 0
