from aiogram.types import CallbackQuery, Message
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp
from filters import IsPrivate

from keyboards.default.default_btn_uz import main_menu_ru, ariza_ru
from keyboards.inline.inline_btn_uz import language, lang_text




####################  Bot haqida ###################
@dp.callback_query_handler(text="lang_ru")
async def uz_lang(call: CallbackQuery):

	text = "С помощью этого бота вы можете оставить свое Заявление, Жалобу и Предложение на имя ректора или деканата Ташкентского Университета Информационных Технологий имени Мухаммада ал-Хоразмий!!!"
	await call.message.answer(text, reply_markup=main_menu_ru)
	await call.message.delete()
	await call.answer(cache_time=30)
	# await call.answer()


#####################  Tilni o'zgartirish  ###################
@dp.message_handler(IsPrivate(),text="🌐 Изменить язык")
async def choose_lang(message:Message):
	await message.answer(lang_text, reply_markup=language)
   




#####################  Bosh menuga qaytish  ###################
@dp.message_handler(IsPrivate(),text="🔝️ Главное меню")
async def menu(message:Message):

	text = "С помощью этого бота вы можете оставить свое Заявление, Жалобу и Предложение на имя ректора или деканата Ташкентского Университета Информационных Технологий имени Мухаммада ал-Хоразмий!!!"
	await message.answer(text, reply_markup=main_menu_ru)



###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
