""" This module defines the creation of a Flask app with MySQL
"""

# Third-parties
from flask import Blueprint, Flask, g

from src.infra.db.redis import RedisClient

# Locals
from src.infra.db.sqlalchemy import Session


def create_flask_mysql_app(blueprints: list[Blueprint]):
    app = Flask(__name__)

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    @app.before_request
    def before_request():
        """Before Request"""
        g.db = Session()
        g.in_memo_db = RedisClient

    def teardown_request(_unused=False):
        """After Request"""
        dbc = getattr(g, "db", None)
        if dbc is not None:
            dbc.close()

    return app
