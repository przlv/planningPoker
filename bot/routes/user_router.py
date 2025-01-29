from aiogram import F, Router, types
from aiogram.filters import Command, callback_data
from sqlalchemy.ext.asyncio import AsyncSession

from common.enum import RepositoryName
from domain.value_objects import Role
from infrastructure.db import sqlite_session
from services.user_service import UserService

router = Router(name="user")


@router.message(Command("choice_roles"))
async def handle_choice_role(message: types.Message) -> None:
    buttons = [
        types.InlineKeyboardButton(text=role, callback_data=f"user/choice_role/{role}") for role in Role.to_list()
    ]
    inline_keyboard = [buttons[i : i + 3] for i in range(0, len(buttons), 3)]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=inline_keyboard, row_width=3)

    await message.answer("Чтобы участвовать в опросах необходимо выбрать роль", reply_markup=keyboard)


@router.callback_query(F.data.startswith("user/choice_role/"))
async def callback_handler_choice_role(callback_query: types.CallbackQuery) -> None:
    role = callback_query.data.split("/")[-1]
    msg = f"Вы выбрали роль: {role}"

    user_service = UserService(RepositoryName.USERS_REPO)

    async_gen = sqlite_session.get_session()
    async_session = await anext(async_gen)
    try:
        await user_service.set_role(user=callback_query.from_user, role=role, session=async_session)
    except Exception as e:
        msg = f"Произошла ошибка при выборе роли"
    finally:
        await callback_query.answer(msg, show_alert=True)
