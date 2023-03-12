import uuid
from dataclasses import dataclass


@dataclass
class User:
    _id: uuid.UUID
    email: str
