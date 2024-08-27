""" This module defines SQLAlchemy User Model
"""

# Natives
from datetime import datetime

# Third-parties
from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Locals
from src.infra.db.sqlalchemy import Base


class UserSQLAlchemyModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), autoincrement=True, primary_key=True, unique=True
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    password_hash: Mapped[str] = mapped_column(INTEGER(unsigned=True), nullable=False)
    created_at: Mapped[str] = mapped_column(
        INTEGER(unsigned=True), nullable=False, default=datetime.now().timestamp()
    )

    # Backrefs
    urls: Mapped[list["UrlSQLAlchemyModel"]] = (  # noqa: F821 # type: ignore
        relationship(
            "UrlSQLAlchemyModel", back_populates="user", cascade="all, delete-orphan"
        )
    )

    def __repr__(self) -> str:
        return f"{self.username} - {self.email}"
