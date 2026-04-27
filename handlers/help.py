from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def help_cmd(msg: Message):
    await msg.answer(
        "ℹ️ <b>Помощь</b>\n\n"
        "/start — открыть приложение\n"
        "/help — справка",
        parse_mode="HTML"
    )
