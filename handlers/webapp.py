from aiogram import Router
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.filters import Command

router = Router()

@router.message(Command("app"))
async def open_app(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(
                text="📊 Открыть SINOBY App",
                web_app=WebAppInfo(
                    url="https://sinoby.app"  # будет
                )
            )
        ]],
        resize_keyboard=True
    )

    await message.answer(
        "Открыть мини‑приложение:",
        reply_markup=keyboard
    )
