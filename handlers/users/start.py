from aiogram import types
from pprint import pprint as print
from filters import IsPrivate


from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inline_btn_uz import language, lang_text
import asyncio
import sqlite3


from data.config import ADMINS
from loader import dp, db, bot


text = "Assalomu alaykum {} botga xush kelibsiz! \n-----\nПривет {}, добро пожаловать в бот!"
@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
	# print(types)
	    # Foydalanuvchini bazaga qo'shamiz
	name = message.from_user.full_name
	try:
	    db.add_user(id=message.from_user.id,  name=name)
	except sqlite3.IntegrityError as err:
		pass
	    # await bot.send_message(chat_id=ADMINS[0], text=err)

	await message.answer(text.format(message.from_user.full_name, message.from_user.full_name, message.from_user.full_name))
	await asyncio.sleep(1)	
	await message.answer(lang_text, reply_markup=language)

	# await message.answer('<a href="tg://user?id=973108256">inline mention</a>')
	# await message.delete()         ####   foydalanuvchidan kelgan  messageni o'chiradi



# @dp.message_handler(IsPrivate())
# async def bot_add_id(message: types.Message):
# 	name = message.from_user.full_name
# 	try:
# 	    db.add_user(id=message.from_user.id,
# 	                name=name)
# 	except sqlite3.IntegrityError as err:
# 	    # await bot.send_message(chat_id=ADMINS[0], text=err)
# 	    pass

		
	 