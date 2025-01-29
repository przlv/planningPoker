import uuid

from dependency_injector.wiring import Provide
from sqlalchemy.ext.asyncio import AsyncSession

from common import bootstrap, enum
from domain.entities import Role
from infrastructure.db import sqlite_session
from interfaces import abstract_factory
from interfaces.abstract_service import AbstractAsyncService
from models.user import User
from repositories.users_repository import UsersRepository


class UserService(AbstractAsyncService):
    uow_factory: abstract_factory.AbstractFactory = Provide[bootstrap.Bootstrap.alchemy_uow_factory]

    def __init__(self, user_repo: UsersRepository):
        self.user_repo = user_repo

    async def __call__(self, *args, **kwargs):
        pass

    async def register_user(self, user_id: int, username: str) -> User:
        pass

    async def set_role(self, user: int, role: Role, session: AsyncSession):
        uow = await self.uow_factory(session)

        async with uow:
            db = uow.repositories[enum.RepositoryName.USERS_REPO.value]
            res = await db.get_user_by_telegram_id(telegram_id=user.id)
            if len(res) == 0:
                await db.create(
                    User(
                        id=uuid.uuid4(),
                        user_id=user.id,
                        username=user.full_name,
                        role=role,
                    )
                )
            else:
                await db.update(res[0], role)
