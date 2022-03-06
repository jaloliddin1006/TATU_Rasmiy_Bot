from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.data import fakultet_data, fakultet_data_ru



lang_text = "O'zingizga qulay tilni tanlang!(🇺🇿)\n-----\nВыберите удобный Вам язык!(🇷🇺)"

# fakultet_data = {
#     "Dasturiy injiniring":"dekanat_dif",
#     "Kompyuter injiniringi":"dekanat_kif",
#     "Kiberxavfsizlik fakulteti":"dekanat_kiberxavfsizlik",
#     "Telekommunikatsiya texnologiyalari":"dekanat_telekom",
#     "Televizion texnologiyalar":"dekanat_televizion",
#     "Iqtisodiyot va menejment":"dekanat_iqtisod",
#     "Radio va mobil aloqa":"dekanat_radio",
#     "AKT sohasida kasb ta'limi":"dekanat_akt",
#     "TATU-BGUIR qo‘shma axborot texnologiyalari fakulteti":"dekanat_belarus",
# }

# ict_link = InlineKeyboardMarkup(InlineKeyboardButton(text="ICT Academy", url="https://t.me/ictacademy_uz"))





tatu_link = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="🏛 TATU Rasmiy", url="https://t.me/tuituz_official"),
		InlineKeyboardButton(text="⛪️ ICT Academy", url="https://t.me/ictacademy_uz"),
	],

])





ict_link = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="⛪️ ICT Academy", url="https://t.me/ictacademy_uz"),
	],

])






fakultetlar = InlineKeyboardMarkup(row_width=2)

for key, value in fakultet_data.items():
    fakultetlar.insert(InlineKeyboardButton(text=key, callback_data=value))




fakultetlar_ru = InlineKeyboardMarkup(row_width=2)

for key, value in fakultet_data_ru.items():
    fakultetlar_ru.insert(InlineKeyboardButton(text=key, callback_data=value))






language = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="🇺🇿 Uz", callback_data="lang_uz"),
		InlineKeyboardButton(text="🇷🇺 Ru", callback_data="lang_ru"),
		# InlineKeyboardButton(text="🇬🇧 En", callback_data="lang_en"),
	],
])


rektorat_btn = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="👨🏼‍💼 Rektor", callback_data="rektor"),
		InlineKeyboardButton(text="👨‍👨‍👦‍👦 Rektorat", callback_data="rektorant"),
	],

])


rektorat_btn_ru = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="👨🏼‍💼 Ректор", callback_data="rektor"),
		InlineKeyboardButton(text="👨‍👨‍👦‍👦 Ректорат", callback_data="rektorant"),
	],

])


shaxsni_aniqla_rek = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="🧑🏻‍🎓 Ariza yozish", callback_data="shaxsi_malum"),
	],
])

shaxsni_aniqla_rek_ru = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="🧑🏻‍🎓 Написать заявку", callback_data="shaxsi_malum_ru"),
	],
])

shaxsni_aniqla = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="🧑🏻‍🎓 Ariza yozish", callback_data="shaxsi_malum"),
	],
	[
		InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga_dekanat"),
	],
])


shaxsni_aniqla_ru = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="🧑🏻‍🎓 Написать заявку", callback_data="shaxsi_malum_ru"),
	],
	[
		InlineKeyboardButton(text="🔙 Назад", callback_data="ortga_dekanat_ru"),
	],
])





tekshir = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Ha", callback_data="send"),
		InlineKeyboardButton(text="❌ Yo'q", callback_data="wrong"),
	],
])


tekshir_ru = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ да", callback_data="send_ru"),
		InlineKeyboardButton(text="❌ Нет", callback_data="wrong_ru"),
	],
])


tekshir_answer = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Ha", callback_data="answer_yes"),
		# InlineKeyboardButton(text="❌ Yo'q", callback_data="answer_no"),
	],
])

tekshir_answer_ru = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Ha", callback_data="answer_yes_ru"),
		# InlineKeyboardButton(text="❌ Yo'q", callback_data="answer_no_ru"),
	],
])
