from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Bot
from loader import dp
from filters import IsPrivate, IsGroup
from keyboards.default.default_btn_uz import ariza_ru, phone_num_ru, main_menu_ru
from keyboards.inline.inline_btn_uz import shaxsni_aniqla_ru, fakultetlar_ru, tekshir_ru, tekshir_answer_ru, shaxsni_aniqla_rek_ru
from data.data import fakultet_data, fakultet_data_ru
from aiogram.dispatcher import FSMContext
from states.state_data import PersonalDataNone_ru, PersonalData_ru, ru_shaxs
from states.state_data import answer_ru, answer_qayta_ru
from handlers.users.user_count import xabarlar 
from datetime import datetime
import re
from data.config import GROUP_CHAT_ID, BOT_TOKEN
import asyncio
from handlers.users.ariza_uz import user_id_olish
import pytz

bot=Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
PHONE_NUM_2 = r'^[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'




javob_bekor_ru = ReplyKeyboardMarkup(
    keyboard=[
 
        [
            KeyboardButton(text="❌ Arizaga javob bermaslik"), 
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Quidagi tugma orqali javob yozishni bekor qilish mumkin"

)



yana_javob_ru = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✍️ Qo'shimcha javob yozish", callback_data="qoshimcha_javob_yoz_ru"),
	],
])


##################################################################################################
#####################  Ariza yozish bo'limi  ###################
##################################################################################################
@dp.message_handler(IsPrivate(),text="✍️ Написать заявку")
async def ariza_yozish(message:Message):
	await message.answer("К кому вы обращаетесь?", reply_markup=ariza_ru)


##################################################################################################
##################################################################################################
##################### dekanatga Ariza yozish bo'limi  ###################
##################################################################################################
@dp.message_handler(IsPrivate(),text="🤵🏼‍♂️ Кабинет декана")
async def dekanat(message:Message):
	global manzil
	manzil = "Кабинет декана"
	await message.answer("✍️ К какому декану факультета вы хотите обратиться?", reply_markup=fakultetlar_ru)


######### 1-susul ###############################################################################################################################################################

fakultet = ""


for i in fakultet_data_ru:


	@dp.callback_query_handler(text=f'{fakultet_data_ru[i]}')
	# @dp.callback_query_handler(lambda c: c.answer["text"] ==f'{fakultet_data[i]}')
	async def bot_start(call: CallbackQuery,state:FSMContext):
		# print(call.data)
		for x in fakultet_data_ru:
			if call.data == fakultet_data_ru[x]:
				global fakultet
				fakultet = x
			
		await call.message.delete()
		await call.message.answer(f"Вы готовы обратиться к декану {fakultet} факультета?", reply_markup=shaxsni_aniqla_ru)

#######################################################################################################################################################################

	

@dp.callback_query_handler(text="ortga_dekanat_ru")
async def ariza_x(call: CallbackQuery):

	# print(fakultet)

	await call.message.delete()

	await call.message.answer("✍️ К какому декану факультета вы хотите обратиться?", reply_markup=fakultetlar_ru)






##################################################################################################


##################################################################################################
##################################################################################################
##################### rektoratga Ariza yozish bo'limi  ###################
##################################################################################################
@dp.message_handler(IsPrivate(),text="🤵🏼‍♂️ Ректорат")
async def rektorat(message:Message):
	global manzil
	manzil = "Ректорат"
	# print(manzil)
	await message.answer("Готовы подать заявку?", reply_markup=shaxsni_aniqla_rek_ru)




#############################################################################
####################   Ariza shaxsi ma'lum uchun ######################3
##################################################################################################
@dp.callback_query_handler(text="shaxsi_malum_ru", state=None)
async def ariza_malum(call: CallbackQuery):

	await call.message.delete()
	await call.message.answer("🧑🏻‍🎓 Имя и фамилия:", reply_markup=ReplyKeyboardRemove())
	await PersonalData_ru.name.set()



@dp.message_handler(IsPrivate(),state=PersonalData_ru.name)
async def answer_name(message:Message,state:FSMContext):
    name = message.text
    await state.update_data(
        {"name":name}
    )
    await message.answer("👨‍👨‍👦‍👦 Войдите в свою группу:")
    await PersonalData_ru.group.set()



@dp.message_handler(IsPrivate(),state=PersonalData_ru.group)
async def answer_group(message:Message,state:FSMContext):
    group = message.text
    await state.update_data(
        {"group":group}
    )
    await message.answer("📱 Отправьте свой контактный номер, нажав на кнопку ниже:",reply_markup=phone_num_ru,)
    await PersonalData_ru.phone_number.set()
	




@dp.message_handler(IsPrivate(),state=PersonalData_ru.phone_number, content_types=["contact","text"])
async def answer_phone(message:Message, state:FSMContext):
	phone_num = message
	# print(phone_num)
	  
		
	if 'text' in phone_num:
		# print("telefon raqamm")
		# if re.search(PHONE_NUM,phone_num.text) or re.search(PHONE_NUM_2,phone_num.text):
		# 	await state.update_data(
  #           	{"phone_number": phone_num.text}
  #           )
		# 	await message.answer("📅 Ariza matnini kiriting:",reply_markup=ReplyKeyboardRemove())
		# 	await PersonalData_ru.ariza.set()
		# else:
		# 	await message.answer("❌ Noto'g'ri raqam terdingiz!, \nQaytadan kiriting!")
		# 	await PersonalData_ru.phone_number.set()

		await message.reply("👇🏻 Отправить через кнопку ниже!")

	elif phone_num.contact:
		# print(phone_num.contact)
		# if re.search(PHONE_NUM,phone_num.contact.phone_number) :
    
		await state.update_data(
        	{"phone_number": phone_num.contact.phone_number}
        )
		await message.answer("📅 Введите текст заявки:",reply_markup=ReplyKeyboardRemove())
		await PersonalData_ru.ariza.set()


	else:
		await message.answer("❌ Вы набрали неверный номер!, \nВведите снова!")
		await PersonalData_ru.phone_number.set()





@dp.message_handler(IsPrivate(),state=PersonalData_ru.ariza)
async def answer_ariza(message:Message,state:FSMContext):
    ariza = message.text
    global data
    await state.update_data(
        {"ariza": ariza},
    )
 
    data = await state.get_data()
    name = data.get("name")
    group = data.get("group")
    phone_number = data.get("phone_number")
    ariza = data.get("ariza")
    
    my_date = datetime.now(pytz.timezone('Asia/Oral'))
    day = str(my_date)[:16]
    # today = datetime.today()
    # day = f"""{today.strftime('%d')}/{today.strftime('%m')}/{today.strftime('%y')}   {today.strftime('%H')}:{today.strftime('%M')} """

    global msg
    msg = "<b>📌 Yangi ariza!</b> \n\n"	
    msg += f"👨🏼‍💼<b>Kimga: </b>{manzil}\n"
    if fakultet!="":
    	msg += f"🏢<b> Fakultet: </b>{fakultet}\n"
    msg += f"🧑🏻‍🎓<b> Talaba:</b> {name}\n"
    msg += f"👨‍👨‍👦‍👦<b> Guruh:</b> {group}\n"
    msg += f"📱<b> Telefon:</b> {phone_number}\n"
    msg += f"📝<b> Ariza:</b> {ariza}\n"
    msg += f"⏳<b> Sana:</b> {day}\n\n"

    # xabar["message"] = msg

    await message.answer(msg)
    # msg += "Arizani qabul qilasizmi?"
    await state.finish()
    await message.answer("Вы отправите заявку?", reply_markup=tekshir_ru)

##################################################################################################
##################################################################################################

# xabar = {}
# group_msg = ""
@dp.callback_query_handler(text="send_ru")
async def arizani_yuborish(call: CallbackQuery):
	global ariza_soni
	global user_id
	user_id = call.message.chat.id


	#----------------Faylni ochish----------------#
	with open("data\_user_count.txt") as fayl:
	    ariza_soni = int(fayl.read())
	    # print(ariza_soni)
	    ariza_soni += 1
	fayl.close()
	# print(ccc)
	# ------------------FAylga yozish -----------------------#
	with open("data\_user_count.txt",'w') as fayl:
	    fayl.write(f"{ariza_soni}")        #'w'-"write"---Ma'lumotlarni o'chirib yangidan yozadi
	fayl.close()
	#=======================================================#  


	# global xabar
	# xabar["user_chat_id"] = call.message.chat.id

	global xabar
	xabar = xabarlar(ariza_soni, user_id)

	await call.message.delete()
	# user_id_olish(user_id, xabar)

	new_msg = msg.replace("<b>📌 Yangi ariza!</b> ", f"""📌<b> Yangi ariza!</b> \n<b>#️⃣  Ariza raqami:</b> {ariza_soni}        \n<b>🆔 User id: </b><a href="tg://user?id={user_id}">{user_id}</a>""")
	# print(new_msg)
	await bot.send_message(GROUP_CHAT_ID, f"{new_msg} Arizani qabul qilasizmi? ")
	await call.message.answer("✅ Ваша заявка отправлена!",reply_markup=main_menu_ru)




	await call.answer(cache_time=5)
	await call.answer()



@dp.callback_query_handler(text="wrong_ru")
async def arizani_bekor_qilish(call: CallbackQuery):
	# global user_id
	# user_id = call.message.chat.id
	await call.message.delete()
	await call.message.answer("❌ Ваша заявка была отменена!",reply_markup=main_menu_ru)
	await call.answer(cache_time=5)
	await call.answer()

