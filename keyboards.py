from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# button_hi = KeyboardButton('Привет! 👋')
# button_bue = KeyboardButton('Пока! 👋')

# greet_kb = ReplyKeyboardMarkup()

# greet_kb.add(button_hi)
# greet_kb.add(button_bue)

# greet_kb2 = ReplyKeyboardMarkup(
#     resize_keyboard=True, 
#     one_time_keyboard=True
# ).add(button_hi)


'''
методы вставки кнопок
'''
button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')
button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')

markup3 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

markup5.row(button4, button5)
markup5.insert(button6)
markup5.insert(KeyboardButton('lalala'))


'''
отправление геолокации и контакта
'''
markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)

'''
insert
'''
markup_big = ReplyKeyboardMarkup()

markup_big.add(
    button1, button2, button3, button4, button5, button6
)
markup_big.row(
    button1, button2, button3, button4, button5, button6
)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))
