from aiogram import Router, F
import uuid
from aiogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InlineQueryResultVideo,
    InlineQueryResultAudio,
    InlineQueryResultCachedSticker, # Sticker uchun 'Cached' ishlatiladi
    InputTextMessageContent
)


# Routerni yaratamiz
inline_router = Router()

@inline_router.inline_query()
async def show_user_text(inline_query: InlineQuery):
    query_text = inline_query.query or "Nimadir yozing..."

    results = []

    results.append(
        InlineQueryResultPhoto(
            id=str(uuid.uuid4()),
            photo_url="https://picsum.photos/400/300",  # Rasm manzili
            thumbnail_url="https://picsum.photos/100/100",  # Kichik ko'rinishi
            title="Tasodifiy rasm",
            description="Bu rasm haqida qisqacha ma'lumot"
        )
    )

    # 2. Video (URL orqali yoki file_id)
    results.append(
        InlineQueryResultVideo(
            id=str(uuid.uuid4()),
            video_url="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
            mime_type="video/mp4",
            thumbnail_url="https://picsum.photos/100/100",
            title="Ajoyib video",
            description="Video haqida tavsif"
        )
    )

    # 3. Audio (Musiqa)
    results.append(
        InlineQueryResultAudio(
            id=str(uuid.uuid4()),
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            title="Musiqa namunasi",
            performer="Noma'lum ijrochi"
        )
    )

    # 4. Sticker (Faqat file_id orqali ishlaydi)
    # Eslatman: Sticker yuborish uchun avval uning file_id sini bilib olishingiz kerak
    # results.append(
    #     InlineQueryResultCachedSticker(
    #         id=str(uuid.uuid4()),
    #         sticker_file_id="CAACAgIAAxkBAAEJ..."  # Haqiqiy file_id ni qo'ying
    #     )
    # )

    # 5. Matnli xabar (Article) + Emoji
    results.append(
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="Emoji bilan matn 🌟",
            input_message_content=InputTextMessageContent(
                message_text=f"Siz yozgan matn: {query_text} ✨🔥"
            ),
            description="Emoji va matnli xabar yuborish"
        )
    )

    # Natijalarni yuborish
    await inline_query.answer(results=results, cache_time=1)