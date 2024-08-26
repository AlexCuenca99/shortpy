""" This module defines tests cases for the Url entity
"""

# Locals
from .url import Url


def test_url_from_dict(url_fixture):
    """Test the creation of a User instance from a dictionary

    Args:
        url_fixture (dict): Fixture with data of a User
    """
    url = Url.from_dict(url_fixture)

    assert url.id == url_fixture["id"]
    assert url.original_url == url_fixture["original_url"]
    assert url.short_url == url_fixture["short_url"]
    assert url.user_id == url_fixture["user_id"]
    assert url.created_at == url_fixture["created_at"]
    assert url.expires_at == url_fixture["expires_at"]
