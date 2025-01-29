import logging

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.routes import get_all_routes
from common.config import config

logging.basicConfig(level=logging.INFO)


class PokerBot:
    def __init__(self):
        self.bot = Bot(token=config.tg_token)
        self.storage = MemoryStorage()
        self.dp = Dispatcher(storage=self.storage)
        self.dp.include_routers(*get_all_routes())

    async def start_polling(self):
        logging.log(level=logging.INFO, msg="Starting Poker Bot")
        await self.dp.start_polling(self.bot)


poker_bot = PokerBot()
