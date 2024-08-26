""" This module defines the Click entity
"""

# Natives
from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class Click:
    """Click Entity"""

    id: int
    url_id: str
    clicked_at: datetime
    ip_address: str
    user_agent: str

    @classmethod
    def from_dict(cls, data):
        """Convert data from a dictionary"""
        return cls(**data)

    def to_dict(self):
        """Convert data into dictionary"""
        return asdict(self)
