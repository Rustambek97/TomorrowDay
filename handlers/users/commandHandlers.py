from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command('pause', 'stop'))
async def pauseCommand(message: Message):
    await message.answer(text='siz jarayonni to`xtatdingiz')


@router.message(Command('ha'))
@router.message(Command('ma', 'sa'))
async def haCommand(message: Message):
    await message.answer(text='vna gap?')