from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from domain.entities import Card, Role

Base = declarative_base()


class SessionTable(Base):
    """Модель сессии покер-планирования."""

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    creator = Column(Integer, ForeignKey("users.user_id"))
    date_created = Column(DateTime, default=datetime.now)


class UserTable(Base):
    """Модель пользователя в системе."""

    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)
    username = Column(String, index=True)
    role = Column(Enum(Role))


class SessionHistoryTable(Base):
    """Модель истории сессии покер-планирования."""

    __tablename__ = "session_history"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    vote = Column(Enum(Card))
