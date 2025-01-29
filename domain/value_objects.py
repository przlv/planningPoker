from enum import Enum


class Role(str, Enum):
    """Роли пользователей в команде."""

    MANAGER = "Manager"
    BACKEND = "Backend"
    FRONTEND = "Frontend"
    ANALYST = "Analyst"
    TESTER = "Tester"

    @classmethod
    def values(cls):
        return ", ".join([item.value for item in cls])

    @classmethod
    def to_list(cls):
        return [item.value for item in cls]


class Card(str, Enum):
    """Карты для покер-планирования."""

    ONE = "1"
    TWO = "2"
    THREE = "3"
    FIVE = "5"
    EIGHT = "8"
    THIRTEEN = "13"
    TWENTY = "20"
    FORTY = "40"
    INFINITY = "∞"
    QUESTION = "?"
    COFFEE = "☕"
