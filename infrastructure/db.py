from typing import AsyncGenerator, Optional

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from common.config import config
from infrastructure.models import Base


class AlchemySession:
    """
    Класс сессии sqlalchemy
    """

    DB_URL = f"sqlite+aiosqlite:///{config.path_db}"

    def __init__(self, session_name: str) -> None:
        """
        Инициализировать переменные
        :param session_name: Имя сессии
        """

        self.session_name = session_name
        self.engine: AsyncEngine = create_async_engine(self.DB_URL, echo=True if config.dev_mode else False)
        self.session_maker: Optional[async_sessionmaker] = async_sessionmaker(autocommit=False, bind=self.engine)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Получить объект асинхронной сессии
        :return: Объект асинхронной сессии
        """

        if self.session_maker is None:
            raise ValueError("Объект создателя сессии не инициализирован")

        async with self.session_maker() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()

    async def create_tables(self) -> None:
        """
        Создает все таблицы в базе данных, если они еще не созданы.
        :return: None
        """

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Таблицы успешно созданы!")


sqlite_session = AlchemySession("sqlite_session")
