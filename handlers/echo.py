from aiogram import Router
from aiogram.types import Message

from services.user_service import register_user_message

router = Router()


@router.message()
async def echo_handler(message: Message):
    register_user_message(message.from_user.id)
    await message.answer(f"Ты написал: {message.text}")