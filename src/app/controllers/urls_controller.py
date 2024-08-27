""" This module defines the controllers for urls
"""

# Third-parties
from flask.blueprints import Blueprint
from flask.json import jsonify

from src.infra.repositories import UrlSQLAlchemyRepository

# Locals
from src.interactor.usecases.urls import GetUrlsUsecase

urls_v1_blueprint = Blueprint("urls_v1", __name__, url_prefix="/api/v1")


def create_urls_blueprints_v1() -> Blueprint:
    @urls_v1_blueprint.route("/urls", methods=["GET"])
    def get_urls():
        repository = UrlSQLAlchemyRepository()
        usecase = GetUrlsUsecase(repository)

        users = usecase.execute()

        return jsonify(users, 200)

    return urls_v1_blueprint
