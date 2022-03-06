from aiogram import types
from filters import IsPrivate

from loader import dp


# Echo bot
@dp.message_handler(IsPrivate(), content_types="contact")
async def bot_echo(message: types.Message):
	# print(message)
	await message.answer(message.text)
