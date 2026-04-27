from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from bot.config import WEBAPP_URL

router = Router()

@router.message(CommandStart())
async def start(msg: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(
                text="🚀 Открыть приложение",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]],
        resize_keyboard=True
    )

    await msg.answer(
        "Добро пожаловать в <b>bot_new</b>.\n\nОткрой мини‑приложение:",
        parse_mode="HTML",
        reply_markup=kb
    )
``
