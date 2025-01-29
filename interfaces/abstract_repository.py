import abc
from typing import Any, List

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.models import Base


class AbstractRepository(abc.ABC):
    """
    Абстрактный класс репозитория
    """

    def __init__(self, name: str) -> None:
        self.name = name

    @abc.abstractmethod
    def create(self, *args, **kwargs) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class AlchemyRepository(AbstractRepository):
    """
    Базовый класс для репозитория Алхимии
    """

    def __init__(self, name: str, session: AsyncSession) -> None:
        self.session = session
        super().__init__(name)

    @abc.abstractmethod
    def create(self, obj: Base | List[Base]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, *args, **kwargs) -> Any:
        raise NotImplementedError
