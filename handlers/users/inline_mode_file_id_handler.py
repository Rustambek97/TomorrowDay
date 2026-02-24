import uuid
from aiogram import Router
from aiogram.types import (
    InlineQuery,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedVideo,
    InlineQueryResultCachedAudio,
    InlineQueryResultCachedSticker,
    InlineQueryResultCachedDocument,
    InlineQueryResultCachedVoice
)

inline_router = Router()

@inline_router.inline_query()
async def show_cached_medias(inline_query: InlineQuery):
    results = []

    # 1. Rasm (Cached)
    results.append(
        InlineQueryResultCachedPhoto(
            id=str(uuid.uuid4()),
            photo_file_id="AgACAgQAAxkBAAIIt2mULAbMGSiUL3Jzv1lsLbL9FTlKAAIGszEbZnu1UNmKm9YAAZ5d5AEAAwIAA20AAzoE", # Sizdagi rasm file_id
            title="Saqlangan rasm",
            description="Bu bazadagi rasm"
        )
    )

    # 2. Video (Cached)
    results.append(
        InlineQueryResultCachedVideo(
            id=str(uuid.uuid4()),
            video_file_id="BAACAgIAAxkDAAIImWmQLr5QH8lP73Bx5LDnmdyWGUslAALRjAACnYyBSOGC1eKfYad9OgQ", # Sizdagi video file_id
            title="Klip yoki darslik",
            description="Video tavsifi"
        )
    )

    # 3. Audio / Muzika (Cached)
    # results.append(
    #     InlineQueryResultCachedAudio(
    #         id=str(uuid.uuid4()),
    #         audio_file_id="CQACAgIAAxkBAA...", # Sizdagi audio file_id
    #         caption="Musiqani eshitib ko'ring"
    #     )
    # )

    # 4. Sticker (Cached)
    # results.append(
    #     InlineQueryResultCachedSticker(
    #         id=str(uuid.uuid4()),
    #         sticker_file_id="CAACAgIAAxkBAA..." # Sticker file_id
    #     )
    # )

    # 5. Document / Fayl (Cached - PDF, ZIP va h.k)
    # results.append(
    #     InlineQueryResultCachedDocument(
    #         id=str(uuid.uuid4()),
    #         document_file_id="BQACAgIAAxkBAA...", # Fayl file_id
    #         title="Loyiha hujjati (PDF)",
    #         description="Yuklab olish uchun bosing"
    #     )
    # )

    # Natijalarni yuborish
    await inline_query.answer(results=results, cache_time=1)