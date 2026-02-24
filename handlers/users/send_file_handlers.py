import os
from aiogram import Router, F
from aiogram.types import Message, FSInputFile

router = Router()

# 1. Rasm yuborish (Foydalanuvchi "rasm" deb yozsa)
@router.message(F.text.lower() == "rasm")
async def send_photo_example(message: Message):
    # 'downloads/photo.jpg' manzili mavjudligiga ishonch hosil qiling
    photo = FSInputFile("downloads/photos/rasm.jpg")
    await message.answer_photo(
        photo=photo,
        caption="Mana siz so'ragan rasm! 🖼"
    )

# 2. Video yuborish ("video" deb yozsa)
@router.message(F.text.lower() == "video")
async def send_video_example(message: Message):
    video = FSInputFile("downloads/videos/prikol.mp4")
    await message.answer_video(
        video=video,
        caption="Mana bu esa video! 🎬"
    )

# 3. Audio (Musiqa) yuborish ("audio" yoki "musiqa" deb yozsa)
@router.message(F.text.lower().in_(["audio", "musiqa"]))
async def send_audio_example(message: Message):
    audio = FSInputFile("downloads/music/muzik.mp3")
    await message.answer_audio(
        audio=audio,
        caption="Sizga yoqadi degan umiddaman! 🎵"
    )

# 4. Voice (Ovozli xabar) yuborish ("ovoz" deb yozsa)
@router.message(F.text.lower() == "ovoz")
async def send_voice_example(message: Message):
    voice = FSInputFile("downloads/voices/voice.ogg")
    await message.answer_voice(
        voice=voice,
        caption="Bu mening ovozim! 🎤"
    )

# 5. Hujjat yuborish ("fayl" deb yozsa)
@router.message(F.text.lower() == "fayl")
async def send_document_example(message: Message):
    document = FSInputFile("downloads/document.pdf")
    await message.answer_document(
        document=document,
        caption="Mana kerakli hujjat! 📄"
    )