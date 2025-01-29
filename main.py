import asyncio
import logging
import os

from bot.bot import poker_bot
from common import bootstrap
from infrastructure.db import sqlite_session

logging.basicConfig(level=logging.INFO)


async def initialize_db(db_path: str) -> None:
    if not os.path.exists(db_path):
        logging.log(logging.INFO, "Create db SQLite")
        await sqlite_session.create_tables()
    else:
        logging.log(logging.INFO, "DB already exists")


async def main() -> None:
    await initialize_db(db_path="./planningPoker.db")
    await poker_bot.start_polling()


if __name__ == "__main__":
    container = bootstrap.Bootstrap()
    container.wire(modules=["services.user_service"])

    asyncio.run(main())
