from sqlalchemy.ext.asyncio import AsyncSession

from factories import repository_factory
from interfaces import abstract_factory, abstract_unit_of_work
from uow import unit_of_works


class AlchemyUOW(abstract_factory.AbstractFactory):
    def __init__(self, users_repo_factory: repository_factory.UserRepositoryFactory) -> None:
        self.users_repo_factory = users_repo_factory

    async def __call__(self, session: AsyncSession) -> abstract_unit_of_work.AbstractUnitOfWork:
        """
        Создать объект UOW
        :param session: сессия Алхими
        :return: объект UOW
        """

        users_repo = self.users_repo_factory(session)
        uow = unit_of_works.AlchemyOrmUnitOfWork(session)
        uow.add_repos([users_repo])

        return uow
