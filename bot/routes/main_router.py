from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from domain.value_objects import Role

router = Router(name="main")


@router.message(Command("start"))
async def handle_start(message: Message) -> None:
    await message.answer("Привет! Я — бот для покерного планирования задач.")


@router.message(Command("view_roles"))
async def handle_view_roles(message: Message) -> None:
    await message.answer(Role.values())
