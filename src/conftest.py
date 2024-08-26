""" This module defines the basic configurations for the tests.
"""

# Natives
from datetime import datetime

# Third-parties
import pytest


# Fixtures
@pytest.fixture
def user_fixture():
    """Fixture with data of a User

    Returns:
        dict: Dict with the data of a User
    """
    return {
        "id": 1,
        "username": "user",
        "email": "user@user.com",
        "password_hash": "hash",
        "created_at": datetime.now(),
    }


@pytest.fixture
def users_fixture():
    """Fixture with data of a User

    Returns:
        dict: Dict with the data of a User
    """
    return [
        {
            "id": 1,
            "username": "user",
            "email": "user@user.com",
            "password_hash": "hash",
            "created_at": datetime.now(),
        },
        {
            "id": 2,
            "username": "user2",
            "email": "user2@user.com",
            "password_hash": "hash2",
            "created_at": datetime.now(),
        },
    ]


@pytest.fixture
def url_fixture():
    """Fixture with data of a Url

    Returns:
        dict: Dict with the data of a Url
    """
    return {
        "id": 1,
        "original_url": "https://www.google.com",
        "short_url": "http://localhost:5000/1",
        "user_id": 1,
        "created_at": datetime.now(),
        "expires_at": datetime.now(),
    }


@pytest.fixture
def click_fixture():
    """Fixture with data of a Click

    Returns:
        dict: Dict with the data of a Click
    """
    return {
        "id": 1,
        "url_id": 1,
        "clicked_at": datetime.now(),
        "ip_address": "127.0.0.1",
        "user_agent": "Mozilla/5.0",
    }
