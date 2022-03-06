from aiogram import types
from filters import IsGroup

from aiogram.dispatcher.filters.builtin import CommandStart
import asyncio

from loader import dp

@dp.message_handler(IsGroup(),CommandStart())
async def bot_start(message: types.Message):
	
	msg = await message.reply(f"Salom {message.from_user.full_name}! Botni guruhda ishlatish mumkin emas!")
	await asyncio.sleep(1)	
	await message.delete()
	await msg.delete()
