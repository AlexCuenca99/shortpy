""" This module defines the SQLAlchemy implementation of the URL repository.
"""

# Locals
from src.infra.db.sqlalchemy import Session

from ...domain.entities import Url
from ..db.sqlalchemy.models import UrlSQLAlchemyModel


class UrlSQLAlchemyRepository:
    def __init__(self) -> None:
        self._session = Session()

    def _db_to_entity(self, db_row: UrlSQLAlchemyModel) -> Url:
        return Url(
            id=db_row.id,
            original_url=db_row.original_url,
            short_url=db_row.short_url,
            user_id=db_row.user_id,
            created_at=db_row.created_at,
            expires_at=db_row.expires_at,
        )

    def list(self):
        result = self._session.query(UrlSQLAlchemyModel).all()

        if result:
            if len(result) == 1:
                return self._db_to_entity(result[0])
            return [self._db_to_entity(row) for row in result]

        return None
