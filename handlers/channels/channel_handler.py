from aiogram import Router, F, types
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

channel_router = Router()

# Faqat kanallar uchun filtr
channel_router.channel_post.filter(F.chat.type == "channel")

@channel_router.channel_post(F.text)
async def handle_channel_post(message: types.Message):
    """Kanalga post joylanganda unga avtomatik imzo qo'yish"""
    text = message.text + "\n\n— @manikanalim001 bizga obuna bo`ling"
    await message.edit_text(text)


@channel_router.channel_post(F.photo)
async def add_photo_button(message: types.Message):
    """Rasmli postlar tagiga tugma qo'shish"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Do'stlarga ulashish",
                    url=f"https://t.me/share/url?url=https://t.me/manikanalim001/{message.message_id}"
                )
            ]
        ]
    )

    # Rasmli post captioniga tugma ulaymiz
    await message.edit_reply_markup(reply_markup=keyboard)