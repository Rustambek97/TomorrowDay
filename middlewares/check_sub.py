from typing import Any, Awaitable, Callable, Dict, Union
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.enums import ChatMemberStatus
from aiogram.utils.keyboard import InlineKeyboardBuilder

CHANNELS = ["@manikanalim001"]

class CheckSubMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:

        if not event.from_user:
            return await handler(event, data)

        bot = data["bot"]
        user_id = event.from_user.id
        not_subbed_channels = []

        for channel in CHANNELS:
            try:
                # Username @ bilan yoki @ siz bo'lishidan qat'iy nazar tekshiradi
                member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
                if member.status in [ChatMemberStatus.LEFT, ChatMemberStatus.KICKED]:
                    not_subbed_channels.append(channel)
            except Exception as e:
                # Agar bot admin bo'lmasa yoki kanal topilmasa shu yerga tushadi
                print(f"Xatolik yuz berdi: {e}")
                continue

        if not not_subbed_channels:
            # Agar bu 'check_sub' tugmasi bo'lsa va foydalanuvchi a'zo bo'lgan bo'lsa
            if isinstance(event, CallbackQuery) and event.data == "check_sub":
                await event.message.delete()
                await event.message.answer("Xush kelibsiz! Endi botdan foydalanishingiz mumkin.")
            return await handler(event, data)

        # Tugmalarni yasash
        builder = InlineKeyboardBuilder()
        for channel in not_subbed_channels:
            # t.me/ dan keyin @ bo'lmasligi shart, lstrip uni olib tashlaydi
            clean_username = channel.lstrip('@')
            builder.row(
                InlineKeyboardButton(
                    text="Kanalga a'zo bo'lish 📢",
                    url=f"https://t.me/{clean_username}"
                )
            )

        builder.row(
            InlineKeyboardButton(text="Tekshirish ✅", callback_data="check_sub")
        )

        text = "<b>Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:</b>"

        if isinstance(event, Message):
            await event.answer(text, reply_markup=builder.as_markup(), parse_mode="HTML")
        elif isinstance(event, CallbackQuery):
            # Agar hali ham obuna bo'lmagan bo'lsa, ogohlantirish
            await event.answer("Siz hali obuna bo'lmadingiz! ❌", show_alert=True)

        return # Handlerga o'tkazmaymiz