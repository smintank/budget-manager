import asyncio
import logging
import sys
from os import getenv

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers.users import router as user_router

load_dotenv()

TOKEN = getenv('TG_BOT_TOKEN')
dp = Dispatcher()
dp.include_routers(user_router)


async def main() -> None:

    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
