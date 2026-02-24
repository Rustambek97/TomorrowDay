from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

# 1. Global "baza" yaratamiz
# Kalit: kod (masalan "315"), Qiymat: lug'at (file_id va turini saqlash uchun)
temporary_storage = {}

file_router = Router()


@file_router.message(F.photo | F.video | F.document)
async def handle_file_upload(message: Message):
    """Faylni qabul qiladi va unga vaqtinchalik ID biriktiradi"""

    # Fayl turini va ID sini aniqlaymiz
    if message.photo:
        file_id = message.photo[-1].file_id
        file_type = "photo"
    elif message.video:
        file_id = message.video.file_id
        file_type = "video"
    elif message.document:
        file_id = message.document.file_id
        file_type = "document"
    else:
        return

    # Tasodifiy yoki ketma-ket kod yaratish (test uchun oddiy usul)
    # Amalda foydalanuvchi o'zi kod yozishi uchun FSM ishlatish yaxshi
    new_code = str(len(temporary_storage) + 101)  # 101, 102... kabi kodlar

    # GLOBAL LUG'ATGA SAQLASH
    temporary_storage[new_code] = {
        "file_id": file_id,
        "type": file_type
    }

    await message.reply(
        f"✅ Fayl qabul qilindi!\n\n"
        f"🆔 File ID: `{file_id}`\n"
        f"🔢 Saqlash kodi: **{new_code}**\n\n"
        f"Faylni qayta olish uchun shu kodni yuboring."
    )


@file_router.message(F.text.isdigit())
async def send_file_by_code(message: Message):
    """Kod yuborilganda lug'atdan qidirib faylni qaytaradi"""
    code = message.text

    if code in temporary_storage:
        data = temporary_storage[code]
        file_id = data["file_id"]
        file_type = data["type"]

        if file_type == "photo":
            await message.answer_photo(photo=file_id, caption=f"Kod: {code}")
        elif file_type == "video":
            await message.answer_video(video=file_id, caption=f"Kod: {code}")
        elif file_type == "document":
            await message.answer_document(document=file_id, caption=f"Kod: {code}")
    else:
        await message.answer("❌ Kechirasiz, bu kod bilan fayl topilmadi yoki bot qayta ishga tushgan.")