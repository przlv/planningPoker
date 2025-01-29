from dataclasses import dataclass
from typing import Optional

from domain.value_objects import Card, Role


@dataclass
class User:
    """Пользователь в системе."""

    user_id: int
    username: str
    role: Optional[Role] = None
    vote: Optional[Card] = None
