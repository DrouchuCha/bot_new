from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "✅ Бот запущен и работает\n"
        "Напиши что‑нибудь — я отвечу."
    )
