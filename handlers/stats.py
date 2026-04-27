from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.user_service import get_user_stats

router = Router()


@router.message(Command("stats"))
async def stats_handler(message: Message):
    count = get_user_stats(message.from_user.id)

    await message.answer(
        f"📊 <b>Твоя статистика</b>\n"
        f"Сообщений отправлено: <b>{count}</b>"
    )