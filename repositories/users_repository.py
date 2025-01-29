from typing import Any, List

from sqlalchemy import delete, insert, select, sql, update

from domain.value_objects import Role
from infrastructure.models import UserTable
from interfaces import abstract_repository as interface
from models.user import User


class UsersRepository(interface.AlchemyRepository):
    async def create(self, data: User) -> None:
        await self.session.execute(insert(UserTable), data.dict())
        await self.session.commit()

    async def update(self, data: User, new_role: Role) -> None:
        await self.session.execute(update(UserTable).where(UserTable.id == data.id).values(role=new_role))
        await self.session.commit()

    async def get(self) -> List[User]:
        result = await self.session.execute(select(UserTable))
        return result.scalars().all()

    async def get_user_by_telegram_id(self, telegram_id: int) -> User:
        result = await self.session.execute(select(UserTable).where(UserTable.user_id == telegram_id))
        return result.scalars().all()
