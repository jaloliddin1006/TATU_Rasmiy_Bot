from aiogram.types import CallbackQuery, Message
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp
from filters import IsPrivate

from keyboards.default.default_btn_uz import main_menu, ariza
from keyboards.inline.inline_btn_uz import language, lang_text




####################  Bot haqida ###################
@dp.callback_query_handler(text="lang_uz")
async def uz_lang(call: CallbackQuery):

	text = "Bu bot orqali siz Muhammad al-Xorazmiy nomidagi Toshkent Axborot Texnologiyalari Universiteti rektorati yoki dekanatiga o'z Ariza , Shikoyat va Takliflarizni qoldirishiz mumkin!!!"
	await call.message.answer(text, reply_markup=main_menu)
	await call.message.delete()
	await call.answer(cache_time=30)
	# await call.answer()


#####################  Tilni o'zgartirish  ###################
@dp.message_handler(IsPrivate(),text="🌐 Tilni o'zgartirish")
async def choose_lang(message:Message):
	await message.answer(lang_text, reply_markup=language)
   




#####################  Bosh menuga qaytish  ###################
@dp.message_handler(IsPrivate(),text="🔝️ Bosh Menu")
async def menu(message:Message):

	text = "Bu bot orqali siz Muhammad al-Xorazmiy nomidagi Toshkent Axborot Texnologiyalari Universiteti rektorati yoki dekanatiga o'z Ariza , Shikoyat va Takliflarizni qoldirishiz mumkin!!!"
	await message.answer(text, reply_markup=main_menu)



###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
