from typing import List

from aiogram import Router

from bot.routes.main_router import router as main_router
from bot.routes.user_router import router as user_router


def get_all_routes() -> List[Router]:
    routers = [
        main_router,
        user_router,
    ]
    return routers
