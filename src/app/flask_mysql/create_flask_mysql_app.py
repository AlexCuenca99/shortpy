""" This module defines the creation of a Flask app with MySQL
"""

# Third-parties
from flask import Blueprint, Flask, g


def create_flask_mysql_app(blueprints: list[Blueprint]):
    app = Flask(__name__)

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    @app.before_request
    def before_request():
        """Before Request"""
        # g.db = Session()

    def teardown_request(_unused=False):
        """After Request"""
        dbc = getattr(g, "db", None)
        if dbc is not None:
            dbc.close()

    return app
