""" This module defines the usecases for getting URLs.
"""

# Locals
from src.infra.repositories import UrlSQLAlchemyRepository


class GetUrlsUsecase:
    def __init__(self, url_sqlalchemy_repository: UrlSQLAlchemyRepository) -> None:
        self.url_sqlalchemy_repository = url_sqlalchemy_repository

    def execute(self):
        return self.url_sqlalchemy_repository.list()
