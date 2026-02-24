from aiogram.filters import Command, StateFilter
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default.register_reply_button import cancel_kb, phone_kb
from keyboards.inline.register_inline_button import confirm_inline_kb

router = Router()

USERNAME_REGEX = r'^[a-zA-Z0-9_]{3,20}$' # 3-20 ta belgi, faqat harf, raqam va pastki chiziq
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^(\+998|998)\d{9}$' # +998901234567 yoki 998901234567 formatida

class Register(StatesGroup):
    username = State()
    email = State()
    phone = State()

@router.message(Command('register'))
async def registerHandler(message: Message, state: FSMContext):
    await message.answer(text='username kiriting', reply_markup=cancel_kb)
    await state.set_state(Register.username)

@router.message(F.text == "❌ Bekor qilish")
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Jarayon bekor qilindi.", reply_markup=ReplyKeyboardRemove())

@router.callback_query(F.data == "confirm_reg")
async def confirm_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Tasdiqlandi!")
    await state.clear()

@router.callback_query(F.data == "cancel_reg")
async def confirm_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.clear()
    await callback.answer("Ro'yxatdan o'tish bekor qilindi", show_alert=True)

@router.message(Register.username, F.text.regexp(USERNAME_REGEX))
async def usernameHandler(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer(text='email kiriting')
    await state.set_state(Register.email)

@router.message(Register.username) # Regexga tushmagan har qanday xabar uchun
async def invalid_username(message: Message):
    await message.answer(text="Username xato! Faqat harf va raqamdan foydalaning (3-20 ta belgi).")

@router.message(Register.email, F.text.regexp(EMAIL_REGEX))
async def emailHandler(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(text='Telefon raqamingizni kiriting (+998XXXXXXXXX):', reply_markup=phone_kb)
    await state.set_state(Register.phone)

@router.message(Register.email)
async def invalid_email(message: Message):
    await message.answer(text="Email xato kiritildi! Iltimos, haqiqiy email manzilingizni yozing.")

@router.message(Register.phone, F.text.regexp(PHONE_REGEX))
async def phoneHandler(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer(text="Siz muvafaqqiyatli ro'yxatdan o'tdingiz")
    data = await state.get_data()
    await message.answer(
        text=f"Sizning ma'lumotlaringiz \nusername: {data['username']} \nemail: {data['email']} \nphone: {data['phone']}",
        reply_markup=confirm_inline_kb
    )
    await state.clear()

@router.message(Register.phone)
async def invalid_phone(message: Message):
    await message.answer(text="Telefon raqami xato! Namuna: +998901234567")
