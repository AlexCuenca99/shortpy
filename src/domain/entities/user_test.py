""" This module defines tests cases for the User entity
"""

# Locals
from .user import User


def test_user_from_dict(user_fixture):
    """Test the creation of a User instance from a dictionary

    Args:
        user_fixture (dict): Fixture with data of a User
    """
    user = User.from_dict(user_fixture)

    assert user.id == user_fixture["id"]
    assert user.username == user_fixture["username"]
    assert user.email == user_fixture["email"]
    assert user.password_hash == user_fixture["password_hash"]
    assert user.created_at == user_fixture["created_at"]
