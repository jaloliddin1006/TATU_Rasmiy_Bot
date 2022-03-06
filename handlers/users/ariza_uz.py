from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Bot
import sqlite3
from loader import dp, db, bot
from filters import IsPrivate, IsGroup
from keyboards.default.default_btn_uz import ariza, phone_num, main_menu
from keyboards.inline.inline_btn_uz import shaxsni_aniqla, fakultetlar, tekshir, tekshir_answer,shaxsni_aniqla_rek
from data.data import fakultet_data
from aiogram.dispatcher import FSMContext
from states.state_data import PersonalDataNone, PersonalData
from states.state_data import answer, answer_qayta
from handlers.users.user_count import xabarlar 
from datetime import datetime
import re
from data.config import GROUP_CHAT_ID, BOT_TOKEN
import asyncio
import json
import pytz

bot=Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
PHONE_NUM_2 = r'^[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'




javob_bekor = ReplyKeyboardMarkup(
    keyboard=[
 
        [
            KeyboardButton(text="❌ Arizaga javob bermaslik"), 
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Quidagi tugma orqali javob yozishni bekor qilish mumkin"

)



yana_javob = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✍️ Qo'shimcha javob yozish", callback_data="qoshimcha_javob_yoz"),
	],
])

manzil = ""

##################################################################################################
#####################  Ariza yozish bo'limi  ###################
##################################################################################################
@dp.message_handler(IsPrivate(),text="✍️ Ariza yozish")
async def ariza_yozish(message:Message):
	name = message.from_user.full_name
	try:
	    db.add_user(id=message.from_user.id,
	                name=name)
	except sqlite3.IntegrityError as err:
		pass

	await message.answer("Kimga ariza yozasiz?", reply_markup=ariza)


##################################################################################################
##################################################################################################
##################### dekanatga Ariza yozish bo'limi  ###################
##################################################################################################
@dp.message_handler(IsPrivate(),text="🤵🏼‍♂️ Dekanat")
async def dekanat(message:Message):
	global manzil
	manzil = "Dekanat"
	await message.answer("✍️ Qaysi fakultet dekaniga ariza yozmoqchisiz?", reply_markup=fakultetlar)

######### 1-susul ###############################################################################################################################################################

fakultet = ""


for i in fakultet_data:


	@dp.callback_query_handler(text=f'{fakultet_data[i]}')
	# @dp.callback_query_handler(lambda c: c.answer["text"] ==f'{fakultet_data[i]}')
	async def bot_start(call: CallbackQuery):
		# print(call.data)
		for x in fakultet_data:
			if call.data == fakultet_data[x]:
				global fakultet
				fakultet = x
		await call.message.delete()
		await call.message.answer(f"{fakultet} fakultet dekaniga ariza yozishga tayyormisiz?", reply_markup=shaxsni_aniqla)
	

#######################################################################################################################################################################

	


@dp.callback_query_handler(text="ortga_dekanat")
async def ariza_x(call: CallbackQuery):

	# print(fakultet)

	await call.message.delete()

	await call.message.answer("✍️ Qaysi fakultet dekaniga ariza yozmoqchisiz?", reply_markup=fakultetlar)








##################################################################################################


##################################################################################################
##################################################################################################
##################### rektoratga Ariza yozish bo'limi  ###################
##################################################################################################
@dp.message_handler(IsPrivate(),text="🤵🏼‍♂️ Rektorat")
async def rektorat(message:Message):
	global manzil
	manzil = "Rektorat"
	await message.answer("Ariza yozishga tayyormisiz?", reply_markup=shaxsni_aniqla_rek)







#############################################################################
####################   Ariza shaxsi ma'lum uchun ######################3
##################################################################################################
@dp.callback_query_handler(text="shaxsi_malum", state=None)
async def ariza_malum(call: CallbackQuery):

	await call.message.delete()
	await call.message.answer("🧑🏻‍🎓 Ism Familiyangiz:", reply_markup=ReplyKeyboardRemove())
	await PersonalData.name.set()



@dp.message_handler(IsPrivate(),state=PersonalData.name)
async def answer_name(message:Message,state:FSMContext):
    name = message.text
    await state.update_data(
        {"name":name}
    )
    await message.answer("👨‍👨‍👦‍👦 Guruhingizni kiriting:")
    await PersonalData.group.set()



@dp.message_handler(IsPrivate(),state=PersonalData.group)
async def answer_group(message:Message,state:FSMContext):
    group = message.text
    await state.update_data(
        {"group":group}
    )
    await message.answer("📱 O'z telefon raqamingizni quidagi tugmani bosib o'z kontaktingizni yuboring:",reply_markup=phone_num,)
    await PersonalData.phone_number.set()
	




@dp.message_handler(IsPrivate(),state=PersonalData.phone_number, content_types=["contact","text"])
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
		# 	await PersonalData.ariza.set()
		# else:
		# 	await message.answer("❌ Noto'g'ri raqam terdingiz!, \nQaytadan kiriting!")
		# 	await PersonalData.phone_number.set()

		await message.reply("👇🏻 Quidagi tugma orqali jo'nating!")


	elif phone_num.contact:
		# print(phone_num.contact)
		# if re.search(PHONE_NUM,phone_num.contact.phone_number) :
    
		await state.update_data(
        	{"phone_number": phone_num.contact.phone_number}
        )
		await message.answer("📅 Ariza matnini kiriting:",reply_markup=ReplyKeyboardRemove())
		await PersonalData.ariza.set()


	else:
		await message.answer("❌ Noto'g'ri raqam terdingiz!, \nQaytadan kiriting!")
		await PersonalData.phone_number.set()





@dp.message_handler(IsPrivate(),state=PersonalData.ariza)
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
    await message.answer("Arizani yuborasizmi?", reply_markup=tekshir)

##################################################################################################
##################################################################################################

# xabar = {}
# group_msg = ""
@dp.callback_query_handler(text="send")
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
	user_id_olish(user_id,xabar)


	new_msg = msg.replace("<b>📌 Yangi ariza!</b> ", f"""📌<b> Yangi ariza!</b> \n<b>#️⃣  Ariza raqami:</b> {ariza_soni}        \n<b>🆔 User id: </b><a href="tg://user?id={user_id}">{user_id}</a>""")
	# print(new_msg)
	await bot.send_message(GROUP_CHAT_ID, f"{new_msg} Arizani qabul qilasizmi? ")
	await call.message.answer("✅ Arizangiz yuborildi!",reply_markup=main_menu)




	await call.answer(cache_time=5)
	await call.answer()



@dp.callback_query_handler(text="wrong")
async def arizani_bekor_qilish(call: CallbackQuery):
	# global user_id
	# user_id = call.message.chat.id
	await call.message.delete()
	await call.message.answer("❌ Arizangiz bekor qilindi!",reply_markup=main_menu)
	await call.answer(cache_time=5)
	await call.answer()



###############  ANSWER to group ###############################################
###############  ANSWER to group ###############################################
###############  ANSWER to group ###############################################
def user_id_olish(idu,xabar):
	# global xabar
	global user_id
	user_id = idu
	xabar = xabar

# @dp.callback_query_handler(text="answer_yes",state =None)
# async def arizani_yuborish(call: CallbackQuery):
# 	# print("answer ishlayapti")

@dp.message_handler(IsGroup(), is_reply=True)
async def javob(message:Message):
	try:
		 #----------------Faylni ochish----------------#
		with open("data\_user_id.txt") as fayl:
			xabar = json.loads(fayl.read())
		# js = json.loads(data)

		# print(ariza_soni)
		# xabar[f"{soni}"]=id
		fayl.close()

		# print(message.reply_to_message.text)
		global asl_msg
		asl_msg = message.reply_to_message
		global ariza_raqami
		ariza_raqami = int(asl_msg.text[34:39])
		# print(ariza_raqami)


		# global javob_msg
		# javob_msg = await message.reply(f"{ariza_raqami} - arizaga javob yozing")

		# await answer.answer.set()


		if "✅ Qabul qilindi" in asl_msg.text:
			# print("ha")
			ans_msg = "\n\n"
		else:
			ans_msg = """\n       <b>Status: </b> ✅ Qabul qilindi \n\n"""
			# print("yo'q")


	# @dp.message_handler(state=answer.answer)
	# async def send_answer(message:Message, state=FSMContext):
		userid = xabar[f"{int(asl_msg.text[34:39])}"]
		answer = message.text
		# await state.update_data(
		#     {"answer": answer},
		# )

		await asl_msg.delete()
		# await javob_msg.delete()
		await message.delete()
		# print("o'chirildi")
		ariza_matn = asl_msg.text.replace("Arizani qabul qilasizmi?", "")
		ariza_matn = ariza_matn.replace(f"🆔 User id: {userid}", f"""<b>🆔 User id: </b><a href="tg://user?id={userid}">{userid}</a>""")


		today = datetime.today()
		day = f"""{today.strftime('%d')}/{today.strftime('%m')}/{today.strftime('%y')}   {today.strftime('%H')}:{today.strftime('%M')} """



		
		# ans_msg += f"👨🏼‍💼 <b>Qabul qiluvchi:</b> Qabulxona\n"
		ans_msg += f"✍️ <b>Javob:</b> {answer}\n"
		ans_msg += f"⏳ <b>Vaqt:</b> {day}\n"
		await message.answer(ariza_matn + ans_msg)

		# x = ariza_matn.find("<b>#️⃣ Ariza raqami:</b> ")

		# userid = xabar[f"{int(ariza_matn[34:39])}"]

		await bot.send_message(userid, ans_msg)

		
		
	except Exception as e:
		# print(e)
		pass