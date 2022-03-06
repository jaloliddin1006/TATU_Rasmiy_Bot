from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ℹ️ Ma'lumot"),           
            KeyboardButton(text="✍️ Ariza yozish"),           
             
        ],
        [
            KeyboardButton(text="🌐 Tilni o'zgartirish"), 
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Menulardan birini tanlang"

)


main_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ℹ️ Информация"),           
            KeyboardButton(text="✍️ Написать заявку"),           
             
        ],
        [
            KeyboardButton(text="🌐 Изменить язык"), 
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите одно из меню"

)


info_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏛 TATU haqida"),           
            KeyboardButton(text="👨🏼‍💼️ Rektorat"),           
             
        ],
        [
            KeyboardButton(text="👨🏼‍💼️ Dekanat"),           
            KeyboardButton(text="ℹ️ Mualliflar haqida"),           
             
        ],
        [
            KeyboardButton(text="🔝️ Bosh Menu"),           

        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Bo'limlardan birini tanlang"
)

info_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏛 О ТАТУ"),           
            KeyboardButton(text="👨🏼‍💼️ Ректорат"),           
             
        ],
        [
            KeyboardButton(text="👨🏼‍💼️ Кабинет декана"),           
            KeyboardButton(text="ℹ️ Об авторах"),           
             
        ],
        [
            KeyboardButton(text="🔝️ Главное меню"),           

        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите один из разделов"
)



ariza = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤵🏼‍♂️ Rektorat"),           
            KeyboardButton(text="🤵🏼‍♂️ Dekanat"),           
             
        ],
        [
            KeyboardButton(text="🔝️ Bosh Menu"),           

        ],
       
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kimga ariza yozmoqchisiz?"

)


ariza_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤵🏼‍♂️ Ректорат"),           
            KeyboardButton(text="🤵🏼‍♂️ Кабинет декана"),           
             
        ],
        [
            KeyboardButton(text="🔝️ Главное меню"),           

        ],
       
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="К кому вы хотите обратиться?"

)



phone_num = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📲 Telefon raqamimni yuborish",request_contact=True),           
        ],
    ],
    resize_keyboard=True
)



phone_num_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📲 Отправить мой номер телефона",request_contact=True),           
        ],
    ],
    resize_keyboard=True
)
