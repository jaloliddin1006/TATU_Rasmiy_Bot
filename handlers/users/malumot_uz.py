from aiogram.types import Message, CallbackQuery
from aiogram import types, Bot
from loader import dp
import re
from data.config import BOT_TOKEN
from filters import IsPrivate
from keyboards.default.default_btn_uz import info_menu
from keyboards.inline.inline_btn_uz import rektorat_btn, fakultetlar, ict_link, tatu_link
from states.state_data import InfoDekanat
from aiogram.dispatcher import FSMContext
from data.data import prorektorlar, dekanat_data, fakultet_data, rektor_data, mualliflar, tatu_haqida, dekanat_info

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)





#####################  Malumot bo'limi  ###################
@dp.message_handler(IsPrivate(),text="ℹ️ Ma'lumot")
async def malumot(message:Message):
	await message.answer("Qanday ma'lumot izlayapsiz?", reply_markup=info_menu)


@dp.message_handler(IsPrivate(),text="ℹ️ Mualliflar haqida")
async def malumot(message:Message):
	
	await bot.send_photo(chat_id=message.chat.id, photo=open('media/photo/ict_info.jpg', 'rb'), caption=mualliflar, reply_markup=ict_link)


#################################################################################################################
#####################  TATU haqida  ###################
@dp.message_handler(IsPrivate(),text="🏛 TATU haqida")
async def tatu_info(message:Message):
	# await bot.send_photo(chat_id=message.chat.id, photo=open('media/photo/info_tatu.jpg', 'rb'), caption=tatu_info)
	await bot.send_photo(chat_id=message.chat.id, photo=open('media/photo/info_tatu2.jpg', 'rb'), caption=tatu_haqida, reply_markup=tatu_link)


#################################################################################################################
#####################  Rektorat bo'limi  ###################
#################################################################################################################
@dp.message_handler(IsPrivate(),text="👨🏼‍💼️ Rektorat")
async def rektorat_tanla(message:Message):
	await message.answer("Rektorat bo'limi", reply_markup=rektorat_btn)





####################  Rektor haqida ###################
@dp.callback_query_handler(text="rektor")
async def rektor(call: CallbackQuery):

	await types.ChatActions.upload_photo()
	media = types.MediaGroup()
	media.attach_photo(types.InputFile('media/photo/maxkamov.jpg'), rektor_data)
	await call.message.answer_media_group(media)
	await call.message.delete()

	# await call.message.answer(text, reply_markup=info_menu)
	await call.answer(cache_time=30)

#################################################################################################################


####################  Rektorlar haqida ###################
@dp.callback_query_handler(text="rektorant")
async def rektor(call: CallbackQuery):

	await call.message.delete()
	for a in range(1, 6):

		await types.ChatActions.upload_photo()
		media = types.MediaGroup()
		media.attach_photo(types.InputFile(f'media/photo/prorektor{a}.jpg'), prorektorlar[f"prorektor{a}"])
		await call.message.answer_media_group(media)

		# await call.message.answer(text, reply_markup=info_menu)
	await call.answer(cache_time=30)

#################################################################################################################






#################################################################################################################
#####################  Dekanat bo'limi  ###################
#################################################################################################################
@dp.message_handler(IsPrivate(),text="👨🏼‍💼️ Dekanat",state=None)
async def dekanat_tanla(message:Message):
	await message.answer("Qaysi fakultet dekani haqida ma'lumot olmoqchisiz:", reply_markup=fakultetlar)
	await InfoDekanat.name.set()

########################### Fakultet dekanlari ######################################################################################



############### dif##########################################3
@dp.callback_query_handler(text="dekanat_dif",state=InfoDekanat.name)
async def fakultet_infosi(call: CallbackQuery,state:FSMContext):
	await call.message.delete()
	data = dekanat_info["dekanat_dif"]
	await call.message.answer("Dasturiy injiniringi fakulteti haqida")
	await bot.send_photo(chat_id=call.message.chat.id, photo=open('media/photo/info_tatu2.jpg', 'rb'), caption=data["dekanat_dif_info"])
	await call.message.answer("MA'MURIYAT")

	for i in range(1,5):
		await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'media/photo/dekanat_dif_dekan{i}.jpg', 'rb'), caption=data[f"dekan{i}"])

	await state.finish()


########################### kif #######################################
@dp.callback_query_handler(text="dekanat_kif",state=InfoDekanat.name)
async def fakultet_infosi(call: CallbackQuery,state:FSMContext):
	await call.message.delete()
	data = dekanat_info["dekanat_kif"]
	await call.message.answer("Kompyuter injiniringi fakulteti haqida")
	await bot.send_photo(chat_id=call.message.chat.id, photo=open('media/photo/info_tatu2.jpg', 'rb'), caption=data["dekanat_kif_info"])
	await call.message.answer("MA'MURIYAT")

	for i in range(1,5):
		await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'media/photo/dekanat_kif_dekan{i}.jpg', 'rb'), caption=data[f"dekan{i}"])


	await state.finish()


################## dekanat_kiberxavfsizlik ################################

@dp.callback_query_handler(text="dekanat_kiberxavfsizlik",state=InfoDekanat.name)
async def fakultet_infosi(call: CallbackQuery,state:FSMContext):
	await call.message.delete()
	data = dekanat_info["dekanat_kiberxavfsizlik"]
	# cap = 
	await call.message.answer("Kiberxavfsizlik fakulteti haqida")
	await bot.send_photo(chat_id=call.message.chat.id, photo=open('media/photo/info_tatu2.jpg', 'rb'), caption=data["dekanat_kiberxavfsizlik_info"])
	await call.message.answer(data["dekanat_kiberxavfsizlik_info2"])

	await call.message.answer("MA'MURIYAT")

	for i in range(1,5):
		await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'media/photo/dekanat_kiberxavfsizlik_dekan{i}.jpg', 'rb'), caption=data[f"dekan{i}"])

	await state.finish()

########################## dekanat_telekom ##################
@dp.callback_query_handler(text="dekanat_telekom",state=InfoDekanat.name)
async def fakultet_infosi(call: CallbackQuery,state:FSMContext):
	await call.message.delete()
	data = dekanat_info["dekanat_telekom"]
	await call.message.answer("Telekommunikatsiya texnologiyalari  fakulteti haqida")
	await bot.send_photo(chat_id=call.message.chat.id, photo=open('media/photo/info_tatu2.jpg', 'rb'), caption=data["dekanat_telekom_info"])
	await call.message.answer(data["dekanat_telekom_info2"])

	await call.message.answer("MA'MURIYAT")

	for i in range(1,5):
		await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'media/photo/dekanat_telekom_dekan{i}.jpg', 'rb'), caption=data[f"dekan{i}"])

	await state.finish()




########################## dekanat_televizion ##################
@dp.callback_query_handler(text="dekanat_televizion",state=InfoDekanat.name)
async def fakultet_infosi(call: CallbackQuery,state:FSMContext):
	await call.message.delete()
	data = dekanat_info["dekanat_televizion"]
	await call.message.answer("Televizion texnologiyalari fakulteti haqida")
	await bot.send_photo(chat_id=call.message.chat.id, photo=open('media/photo/info_tatu2.jpg', 'rb'), caption=data["dekanat_televizion_info"])
	await call.message.answer("MA'MURIYAT")

	for i in range(1,4):
		await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'media/photo/dekanat_televizion_dekan{i}.jpg', 'rb'), caption=data[f"dekan{i}"])

	await state.finish()



########################## dekanat_iqtisod ##################
@dp.callback_query_handler(text="dekanat_iqtisod",state=InfoDekanat.name)
async def fakultet_infosi(call: CallbackQuery,state:FSMContext):
	await call.message.delete()
	data = dekanat_info["dekanat_iqtisod"]
	await call.message.answer("Iqtisodiyot va menejment fakulteti   haqida")
	await bot.send_photo(chat_id=call.message.chat.id, photo=open('media/photo/info_tatu2.jpg', 'rb'), caption=data["dekanat_iqtisod_info"])
	await call.message.answer("MA'MURIYAT")

	for i in range(1,4):
		await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'media/photo/dekanat_akt_dekan{i}.jpg', 'rb'), caption=data[f"dekan{i}"])

	await state.finish()



########################## dekanat_radio ##################
@dp.callback_query_handler(text="dekanat_radio",state=InfoDekanat.name)
async def fakultet_infosi(call: CallbackQuery,state:FSMContext):
	await call.message.delete()
	data = dekanat_info["dekanat_radio"]
	await call.message.answer("Radio va mobil aloqa fakulteti fakulteti haqida")
	await bot.send_photo(chat_id=call.message.chat.id, photo=open('media/photo/info_tatu2.jpg', 'rb'), caption=data["dekanat_radio_info"])
	await call.message.answer("MA'MURIYAT")

	for i in range(1,4):
		await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'media/photo/dekanat_radio_dekan{i}.jpg', 'rb'), caption=data[f"dekan{i}"])

	await state.finish()



########################## dekanat_akt ##################
@dp.callback_query_handler(text="dekanat_akt",state=InfoDekanat.name)
async def fakultet_infosi(call: CallbackQuery,state:FSMContext):
	await call.message.delete()
	data = dekanat_info["dekanat_akt"]
	await call.message.answer("AKT sohasida kasb ta'limi   fakulteti haqida")
	await bot.send_photo(chat_id=call.message.chat.id, photo=open('media/photo/info_tatu2.jpg', 'rb'), caption=data["dekanat_akt_info"])
	await call.message.answer("MA'MURIYAT")

	for i in range(1,4):
		await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'media/photo/dekanat_akt_dekan{i}.jpg', 'rb'), caption=data[f"dekan{i}"])

	await state.finish()




########################## dekanat_belarus ##################
@dp.callback_query_handler(text="dekanat_belarus",state=InfoDekanat.name)
async def fakultet_infosi(call: CallbackQuery,state:FSMContext):
	await call.message.delete()
	data = dekanat_info["dekanat_belarus"]
	await call.message.answer("TATU-BGUIR qo‘shma axborot texnologiyalari fakulteti haqida")
	await bot.send_photo(chat_id=call.message.chat.id, photo=open('media/photo/_belarus.jpg', 'rb'), caption=data["dekanat_belarus_info"])
	await call.message.answer(data["dekanat_belarus_info2"])
	await call.message.answer(data["dekanat_belarus_info3"])

	await call.message.answer("MA'MURIYAT")

	for i in range(1,5):
		await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'media/photo/dekanat_belarus_dekan{i}.jpg', 'rb'), caption=data[f"dekan{i}"])

	await state.finish()
