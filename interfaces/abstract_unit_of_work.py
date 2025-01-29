from __future__ import annotations

import abc

from interfaces import abstract_repository


class AbstractUnitOfWork(abc.ABC):
    """
    Абстрактный класс для unit of work
    """

    def __init__(self) -> None:
        self.repositories = {}

    def add_repos(self, repositories: list[abstract_repository.AbstractRepository]) -> None:
        for repository in repositories:
            self.repositories[repository.name] = repository

    async def __aenter__(self) -> AbstractUnitOfWork:
        return self

    async def __aexit__(self, *args) -> None:
        await self.rollback()

    @abc.abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError
