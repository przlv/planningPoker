import abc


class AbstractFactory(abc.ABC):
    """
    Абстрактный класс фабрики
    """

    @abc.abstractmethod
    def __call__(self, *args, **kwargs) -> any:
        """
        Создать экземпляр объекта
        :return: экземпляр объекта
        """

        raise NotImplementedError
