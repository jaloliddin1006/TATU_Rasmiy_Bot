# from aiogram import types, Bot
# from loader import dp
# from handlers.users.ariza_uz import fakultet, xabar
# from filters import IsGroup
# from data.config import BOT_TOKEN
# from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message
# from states.state_data import PersonalDataNone, PersonalData
# from aiogram.dispatcher import FSMContext
# from states.state_data import answer
# from datetime import datetime

# bot=Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# @dp.message_handler(text="salom")
# async def send_message(message: types.Message,state:FSMContext):
#     print(fakultet)


#     print(xabar["user_chat_id"])
#     print("answer ishlayapti")
#     print(xabar["message"])



# @dp.callback_query_handler(text="answer_yes",state =None)
# async def arizani_yuborish(call: CallbackQuery):
#     print("answer ishlayapti")
#     # msg = xabar["message"]
  
#     # await bot.send_message(user_id, msg)
#     # print(call)
#     global asl_msg
#     asl_msg = call.message

#     global msg1
#     msg1 = str(call.message.text)

 
#     global javob_msg
#     javob_msg = await call.message.reply("Javob yozing")
#     # await call.message.delete()
#     # await call.message.delete()
#     # await call.answer(cache_time=30)
#     await answer.answer.set()


# @dp.message_handler(state=answer.answer)
# async def send_answer(message:Message, state=FSMContext):
#     answer = message.text
#     await state.update_data(
#         {"answer": answer},
#     )
#     # await reply_msg.delete()
#     await javob_msg.delete()
#     await asl_msg.delete()
#     await message.delete()
#     print("o'chirildi")
#     # print(msg1)

#     today = datetime.today()
#     day = f"""{today.strftime('%d')}/{today.strftime('%m')}/{today.strftime('%y')}   {today.strftime('%H')}:{today.strftime('%M')} """

#     # msg = xabar["message"]

#     msg = f"{msg1}\n<b>Status: </b> ✅ Qabul qilindi \n\n"
#     msg += f"👨🏼‍💼 <b>Qabul qiluvchi:</b> {message.from_user.full_name}\n"
#     msg += f"✍️ <b>Javob:</b> {answer}\n"
#     msg += f"⏳ <b>Vaqt:</b> {day}"
#     await message.answer(msg)


#     user_id = xabar['user_chat_id']
#     await bot.send_message(user_id, msg)


#     # await answer.new_msg.set()
    
#     await state.finish()






# @dp.callback_query_handler(text="answer_no")
# async def arizani_yuborish(call: CallbackQuery):
#     print("answer ishlayapti")

#     await call.message.delete()
#     # msg = xabar["message"]
#     print(call.from_user)

#     today = datetime.today()
#     day = f"""{today.strftime('%d')}/{today.strftime('%m')}/{today.strftime('%y')}   {today.strftime('%H')}:{today.strftime('%M')} """

#     msg += f"{msg1}\n<b>Status: </b> ❌ Bekor qilindi \n\n"
#     msg += f"👨🏼‍💼 <b>Kim tomonidan:</b> {call.from_user.full_name}\n"
#     msg += f"⏳ <b>Vaqt:</b> {day}"
#     await call.message.answer(msg)


#     user_id = xabar['user_chat_id']
#     await bot.send_message(user_id, msg)















# @dp.message_handler(state=answer.new_msg)
# async def send_answer(message:Message, state=FSMContext):


#     data = await state.get_data()
#     answer = data.get("answer")
    # new_msg = data.get("new_msg")

    # # await reply_msg.delete()
    # # await javob_msg.delete()

    # msg = xabar["message"]

    # await message.answer(msg)








# @dp.callback_query_handler(text="wrong")
# async def arizani_bekor_qilish(call: CallbackQuery):
  
#     await call.message.delete()
#     await call.message.answer("❌ Arizangiz bekor qilindi!",reply_markup=main_menu)
#     await call.answer(cache_time=30)
#     await call.answer()
