""" This module defines the User entity
"""

# Natives
from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class User:
    """User Entity"""

    id: int
    username: str
    email: str
    password_hash: str
    created_at: datetime

    @classmethod
    def from_dict(cls, data):
        """Convert data from a dictionary"""
        return cls(**data)

    def to_dict(self):
        """Convert data into dictionary"""
        return asdict(self)
