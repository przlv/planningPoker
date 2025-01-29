import abc
from typing import Any


class AbstractSyncService(abc.ABC):
    """
    Интерфейс вызова сервиса
    """

    @abc.abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @abc.abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class AbstractAsyncService(AbstractSyncService, abc.ABC):
    """
    Интерфейс асинхронного вызова сервиса
    """

    @abc.abstractmethod
    async def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError
