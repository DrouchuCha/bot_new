import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.stats import router as stats_router
from handlers.echo import router as echo_router

from services.user_service import init_db


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    # Инициализация базы данных SQLite
    init_db()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    # Регистрируем роутеры
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(stats_router)
    dp.include_router(echo_router)

    logging.info("✅ Бот запущен и работает с SQLite")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())