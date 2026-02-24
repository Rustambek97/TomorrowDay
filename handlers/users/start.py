from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from services.db_api.sqlite import db
router = Router()


@router.message(CommandStart())
async def bot_start(message: Message):
    await message.answer("Salom 👋")
    await db.execute(
        sql="INSERT OR IGNORE INTO Users VALUES (?, ?, ?, ?)",
        parameters=(message.from_user.id, message.from_user.first_name, message.from_user.last_name,message.from_user.username),
        commit=True
    )
