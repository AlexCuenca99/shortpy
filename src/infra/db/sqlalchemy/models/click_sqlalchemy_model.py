""" This module defines SQLAlchemy Click Model
"""

# Third-parties
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Locals
from src.infra.db.sqlalchemy import Base


class ClickSQLAlchemyModel(Base):
    __tablename__ = "clicks"

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), autoincrement=True, primary_key=True, unique=True
    )
    ip_address: Mapped[str] = mapped_column(String(255), nullable=True)
    user_agent: Mapped[str] = mapped_column(String(255), nullable=True)

    # Foreigns
    url_id: Mapped[int] = mapped_column(ForeignKey("urls.id"), nullable=False)

    # Backrefs
    url: Mapped["UrlSQLAlchemyModel"] = relationship(  # noqa: F821 # type: ignore
        "UrlSQLAlchemyModel", back_populates="clicks"
    )

    # Timestamps
    clicked_at: Mapped[str] = mapped_column(INTEGER(unsigned=True), nullable=True)

    def __repr__(self) -> str:
        return f"{self.url_id} - {self.clicked_at}"
