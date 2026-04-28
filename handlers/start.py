from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
)

from bot.config import WEBAPP_URL

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🚀 Открыть приложение",
                    web_app=WebAppInfo(
                        url=WEBAPP_URL,
                    ),
                )
            ]
        ],
        resize_keyboard=True,
    )

    await message.answer(
        "Добро пожаловать в <b>bot_new</b>.\n\n"
        "Нажмите кнопку ниже, чтобы открыть Mini App.",
        parse_mode="HTML",
        reply_markup=keyboard,
    )
``from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
)

from bot.config import WEBAPP_URL

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🚀 Открыть приложение",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ],
        resize_keyboard=True,
    )

    await message.answer(
        "Добро пожаловать в <b>bot_new</b>.\n\n"
        "Нажмите кнопку ниже, чтобы открыть mini app.",
        parse_mode="HTML",
        reply_markup=keyboard,
    )from aiogram import Router
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
