from aiogram.dispatcher.filters.state import StatesGroup,State


class PersonalDataNone(StatesGroup):

    ariza = State()
    num =State()


class PersonalDataNone_ru(StatesGroup):

    ariza = State()
    num =State()



class PersonalData(StatesGroup):

    name = State()
    group = State()
    phone_number = State()
    ariza = State()
    chat_id =State()



class PersonalData_ru(StatesGroup):

    name = State()
    group = State()
    phone_number = State()
    ariza = State()
    chat_id =State()


class ru_shaxs(StatesGroup):

    name = State()
    group = State()
    phone_number = State()
    ariza = State()
  

class InfoDekanat(StatesGroup):

    name = State()
    end = State()
    phone_number = State()
    ariza = State()


class answer(StatesGroup):

    answer = State()
    no = State()
    admin_id = State()
  

class answer_qayta(StatesGroup):

    answer = State()
    no = State()
    admin_id = State()
  


class answer_ru(StatesGroup):

    answer = State()
    no = State()
    admin_id = State()
  

class answer_qayta_ru(StatesGroup):

    answer = State()
    no = State()
    admin_id = State()
  
