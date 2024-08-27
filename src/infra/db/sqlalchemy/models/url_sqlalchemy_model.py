""" This module defines SQLAlchemy URL Model
"""

# Natives
from datetime import datetime

# Third-parties
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Locals
from src.infra.db.sqlalchemy import Base


class UrlSQLAlchemyModel(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), autoincrement=True, primary_key=True, unique=True
    )
    original_url: Mapped[str] = mapped_column(String(2500), nullable=False)
    short_url: Mapped[str] = mapped_column(String(50), nullable=False)

    # Foreigns
    user_id: Mapped[INTEGER] = mapped_column(ForeignKey("users.id"), nullable=False)

    # Backrefs
    user: Mapped[list["UserSQLAlchemyModel"]] = (  # noqa: F821 # type: ignore
        relationship("UserSQLAlchemyModel", back_populates="urls")
    )
    clicks: Mapped[list["ClickSQLAlchemyModel"]] = (  # noqa: F821 # type: ignore
        relationship(
            "ClickSQLAlchemyModel", back_populates="url", cascade="all, delete-orphan"
        )
    )

    # Timestamps
    created_at: Mapped[str] = mapped_column(
        INTEGER(unsigned=True), nullable=False, default=datetime.now().timestamp()
    )
    expires_at: Mapped[str] = mapped_column(
        INTEGER(unsigned=True), nullable=True, default=None
    )

    def __repr__(self) -> str:
        return f"{self.original_url} - {self.short_url}"
