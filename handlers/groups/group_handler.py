from aiogram import Router, F, types
from aiogram.filters import Command
from datetime import datetime, timedelta

# Router yaratamiz
group_router = Router()

# Bot guruhda xabarlarni o'chirishi yoki kanalda post yozishi uchun unga Admin huquqlari berilgan bo'lishi shart.
# F.chat.type == "group" yoki F.chat.type == "channel" orqali bot qayerda javob berishini qat'iy belgilab olishingiz mumkin
# Faqat guruh va superguruhlarda ishlash uchun filtr
group_router.message.filter(F.chat.type.in_({"group", "supergroup"}))

@group_router.message(F.new_chat_members)
async def welcome_new_member(message: types.Message):
    """Yangi foydalanuvchi qo'shilganda salomlashish"""
    for user in message.new_chat_members:
        await message.reply(f"Xush kelibsiz, {user.full_name}!")

@group_router.message(F.left_chat_member)
async def left_member(message: types.Message):
    # Chiqib ketgan xabarini o'chirish
    await message.delete()
    # Yoki xabar yuborish
    # await message.answer(f"{message.left_chat_member.full_name} bizni tark etdi.")


@group_router.message(F.text.contains("reklama"))
async def delete_spam(message: types.Message):
    """Guruhda taqiqlangan so'zlarni o'chirish"""
    await message.delete()
    await message.answer(f"{message.from_user.first_name}, guruhda reklama tarqatmang!")


# 1. Foydalanuvchini guruhdan haydash (BAN)
@group_router.message(Command("ban"), F.reply_to_message)
async def ban_user(message: types.Message):
    # Reply qilingan xabar egasini haydash
    await message.chat.ban(user_id=message.reply_to_message.from_user.id)
    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} guruhdan haydaldi!")


# 2. Foydalanuvchini vaqtincha bloklash (MUTE - 5 daqiqaga)
@group_router.message(Command("mute"), F.reply_to_message)
async def mute_user(message: types.Message):
    until_date = datetime.now() + timedelta(minutes=5)
    permissions = types.ChatPermissions(can_send_messages=False)  # Xabar yuborishni o'chirish

    await message.chat.restrict(
        user_id=message.reply_to_message.from_user.id,
        permissions=permissions,
        until_date=until_date
    )
    await message.answer("Foydalanuvchi 5 daqiqaga 'o'qish' rejimiga o'tkazildi.")

# Xabarni qatib qo'yish (Reply qilingan xabarni)
@group_router.message(Command("pin"), F.reply_to_message)
async def pin_message(message: types.Message):
    await message.reply_to_message.pin()
    await message.answer("Xabar yuqoriga qatib qo'yildi!")

# Guruh nomini o'zgartirish
@group_router.message(Command("set_title"))
async def set_group_title(message: types.Message, command: Command):
    new_title = command.args # /set_title Yangi Nom
    if new_title:
        await message.chat.set_title(new_title)
        await message.answer(f"Guruh nomi '{new_title}'ga o'zgartirildi.")