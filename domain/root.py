from dataclasses import dataclass, field
from typing import Dict, List, Optional

from domain.entities import User
from domain.value_objects import Card, Role


@dataclass
class Session:
    """Сессия голосования"""

    session_id: int
    created_by: int
    users: Dict[int, User] = field(default_factory=dict)
    is_active: bool = False

    def start_session(self, user_id: int):
        """Запускает голосование (только Manager)."""
        pass
