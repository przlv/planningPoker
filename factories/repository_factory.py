from sqlalchemy.ext.asyncio import AsyncSession

from common import enum
from interfaces import abstract_factory, abstract_repository
from repositories import users_repository


class UserRepositoryFactory(abstract_factory.AbstractFactory):
    def __call__(self, session: AsyncSession) -> abstract_repository.AlchemyRepository:
        """
        Создать объект репозитория
        :return: объект репозитория
        """

        return users_repository.UsersRepository(enum.RepositoryName.USERS_REPO.value, session)
