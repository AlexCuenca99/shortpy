""" This module defines the controllers for urls
"""

# Locals
from flask.blueprints import Blueprint

urls_v1_blueprint = Blueprint("urls_v1", __name__, url_prefix="/api/v1")


def create_urls_blueprints_v1() -> Blueprint:
    @urls_v1_blueprint.route("/urls", methods=["GET"])
    def get_urls():
        return "Hello, World!"

    return urls_v1_blueprint
