from dependency_injector import containers, providers

from factories import repository_factory, uow_factory


class Bootstrap(containers.DeclarativeContainer):
    """
    Контейнер с зависимостями
    """

    config = providers.Configuration()

    user_repo_factory = providers.Factory(repository_factory.UserRepositoryFactory)

    alchemy_uow_factory = providers.Factory(uow_factory.AlchemyUOW, users_repo_factory=user_repo_factory)
