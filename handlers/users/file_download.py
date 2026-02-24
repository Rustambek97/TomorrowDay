import os
from aiogram import Router, F, Bot
from aiogram.types import Message

router = Router()

@router.message(F.document)
async def handle_document(message: Message, bot: Bot):
    # 1. Papka mavjudligini tekshirish (agar yo'q bo'lsa yaratadi)
    # os.makedirs("downloads", exist_ok=True)

    # 2. Faylning to'liq yo'li (downloads/fayl_nomi.kengaytma)
    file_name = message.document.file_name
    destination = f"downloads/{file_name}"

    # 3. Yuklab olish
    await bot.download(
        file=message.document.file_id,
        destination=destination
    )

    await message.reply(f"Fayl muvaffaqiyatli saqlandi: {file_name}")


@router.message(F.photo)
async def handle_photo(message: Message, bot: Bot):
    # os.makedirs("downloads/photos", exist_ok=True)

    photo = message.photo[-1]  # Eng kattasi
    destination = f"downloads/photos/{photo.file_unique_id}.jpg"

    await bot.download(file=photo, destination=destination)
    await message.reply("Rasm saqlandi!")


# 1. Video yuklab olish
@router.message(F.video)
async def handle_video(message: Message, bot: Bot):
    os.makedirs("downloads/videos", exist_ok=True)

    # Agar fayl nomi bo'lmasa, file_id dan foydalanamiz
    file_name = message.video.file_name or f"{message.video.file_id}.mp4"
    destination = f"downloads/videos/{file_name}"

    await bot.download(
        file=message.video,
        destination=destination
    )
    await message.reply(f"🎬 Video saqlandi: {file_name}")


# 2. Audio (Musiqa) yuklab olish
@router.message(F.audio)
async def handle_audio(message: Message, bot: Bot):
    os.makedirs("downloads/music", exist_ok=True)

    # Audio obyektida odatda ijrochi va nom bo'ladi
    file_name = message.audio.file_name or f"{message.audio.file_id}.mp3"
    destination = f"downloads/music/{file_name}"

    await bot.download(
        file=message.audio,
        destination=destination
    )
    await message.reply(f"🎵 Audio saqlandi: {file_name}")


# 3. Voice (Ovozli xabar) yuklab olish
@router.message(F.voice)
async def handle_voice(message: Message, bot: Bot):
    os.makedirs("downloads/voices", exist_ok=True)

    # Ovozli xabarlarda file_name bo'lmaydi, ogg formatida bo'ladi
    destination = f"downloads/voices/{message.voice.file_unique_id}.ogg"

    await bot.download(
        file=message.voice,
        destination=destination
    )
    await message.reply("🎤 Ovozli xabar saqlandi!")