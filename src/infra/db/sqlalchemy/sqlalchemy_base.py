""" This module defines base class for SQLAlchemy connection stablishment
"""

# Natives
import logging

# Third-parties
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker

# Locals
from configs import config


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models"""


engine = create_engine(config.DB_URI)
Session = scoped_session(sessionmaker(bind=engine))

try:
    engine.connect()
    logging.info("The connection has been established", end="\n")
except Exception as e:
    logging.info("Connection could not be established due to ", e)
