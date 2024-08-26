""" This module defines tests cases for the Click entity
"""

# Locals
from .click import Click


def test_click_from_dict(click_fixture):
    """Test the creation of a Click instance from a dictionary

    Args:
        click_fixture (dict): Fixture with data of a Click
    """
    click = Click.from_dict(click_fixture)

    assert click.id == click_fixture["id"]
    assert click.url_id == click_fixture["url_id"]
    assert click.clicked_at == click_fixture["clicked_at"]
    assert click.ip_address == click_fixture["ip_address"]
    assert click.user_agent == click_fixture["user_agent"]
