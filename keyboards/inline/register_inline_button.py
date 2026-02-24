from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirm_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="confirm_reg"),
            InlineKeyboardButton(text="🗑 O'chirish", callback_data="cancel_reg")
        ]
    ]
)