""" This module defines the Url entity
"""

# Natives
from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class Url:
    """Url Entity"""

    id: int
    original_url: str
    short_url: str
    user_id: str
    created_at: datetime
    expires_at: datetime

    @classmethod
    def from_dict(cls, data):
        """Convert data from a dictionary"""
        return cls(**data)

    def to_dict(self):
        """Convert data into dictionary"""
        return asdict(self)
