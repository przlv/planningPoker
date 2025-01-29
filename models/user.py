from uuid import UUID

from pydantic import Field

from domain.value_objects import Card, Role
from interfaces import base


class User(base.ModelConfig):
    id: UUID = Field(description="Идентификатор пользователя")
    user_id: int = Field(description="Идентификатор пользователя TelegramId")
    username: str = Field(description="Имя пользователя")
    role: Role = Field(description="Роль")
