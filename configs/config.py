""" This module defines the configuration application file
"""

# Primitives
import os

# Third parties
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

# Retrieve the environment set in docker-compose environment variable
environment = os.getenv("FLASK_ENV", "development")

load_dotenv(f".env.{environment[:3]}")

# Database configurations
DB_USER = os.getenv("MYSQL_USER")
DB_PASS = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = int(os.getenv("MYSQL_PORT", 3306))
DB_DRIVER = os.getenv("MYSQL_DRIVER", "mysql+pymysql")

DB_URI = URL.create(
    drivername=DB_DRIVER,
    username=DB_USER,
    password=DB_PASS,
    database=DB_NAME,
    host=DB_HOST,
    port=DB_PORT,
)

# Redis configurations
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
