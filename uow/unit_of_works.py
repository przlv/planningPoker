from sqlalchemy.ext.asyncio import AsyncSession

from interfaces import abstract_unit_of_work as abs_uow


class AlchemyOrmUnitOfWork(abs_uow.AbstractUnitOfWork):
    """
    Unit of work для работы с репозиториями Алхимии
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

        super().__init__()

    async def __aenter__(self) -> abs_uow.AbstractUnitOfWork:
        return await super().__aenter__()

    async def __aexit__(self, *args) -> None:
        await super().__aexit__(*args)
        await self.session.aclose()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
