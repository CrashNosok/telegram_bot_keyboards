import logging

from aiogram import Bot, executor, Dispatcher, types

import keyboards as kb
import inline_keyboards as inkb

API_TOKEN = 'YOUR API TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    # reply - ответ на сообщение
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


'''
# @dp.message_handler(lambda message: message.text == 'foo')
@dp.message_handler()
async def echo(message: types.Message):
    # answer - просто отправить сообщение
    await message.answer(message.text)
'''


@dp.message_handler(commands=['voice'])
async def process_voice_command(message: types.Message):
    await bot.send_audio(chat_id=message.from_user.id, audio='https://zvukipro.com/uploads/files/2018-12/1545299705_zhenschiny-smejutsja.mp3',
                         reply_to_message_id=message.message_id)


@dp.message_handler(content_types=['sticker'])
async def get_sticker_id(sticker: types.sticker.Sticker):
    bot = Bot.get_current()
    # echo sticker
    # await bot.send_sticker(chat_id=sticker.chat.id, sticker=sticker.sticker.file_id)
   
    # send sticker id
    await bot.send_message(chat_id=sticker.chat.id, text=sticker.sticker.file_id)


@dp.message_handler(content_types=['voice'])
async def get_voice_id(message: types.Voice):
    bot = Bot.get_current()
    await bot.send_voice(chat_id=message.chat.id, voice=message.voice.file_id)
    

'''
# send sticker
@dp.message_handler()
async def send_sticker(message: types.Message):
    # 1 способ по url
    # await message.answer_sticker('https://www.gstatic.com/webp/gallery/1.webp')

    # 2 способ, через бота
    bot = Bot.get_current()
    await bot.send_sticker(chat_id=message.chat.id, sticker='CAADAgADOQADfyesDlKEqOOd72VKAg')
'''


# клавиатура:
@dp.message_handler(commands=['key'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.markup_big)


@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("Убираем шаблоны сообщений", reply_markup=kb.ReplyKeyboardRemove())


'''
inline кнопки:
'''
@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=inkb.inline_kb_full)


'''
обработчик для нажатой кнопки 
'''
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_button1(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    print('---------------')
    print(callback_query)
    print('---------------')
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        # text - высветится после "загрузки" сверху
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')


    # await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
