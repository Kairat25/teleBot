from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
import logging


TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Салам хозяин {message.from_user.full_name}")

@dp.message_handler(commands=['command'])
async def command_push(message: types.Message):
    await bot.send_message(message.chat.id, f"/start, /test1, /test2, /mem, /mem1 {message.from_user.full_name}")


@dp.message_handler(commands=['test1'])
async def quinz_1(message: types.Message):
    question = "Что озночает True в питоне?"
    answers = ['Ритм', 'Да', 'Один', 'Много']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2
                        )

@dp.message_handler(commands=['mem'])
async def mem_1(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1"
    )
    murkup.add(button_call_1)
    mem = open("media/download.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=mem)

@dp.message_handler(commands=['mem1'])
async def mem_2(message: types.Message):
        murkup = InlineKeyboardMarkup()
        button_call_1 = InlineKeyboardButton(
            "NEXT",
            callback_data="button_call_1"
        )
        murkup.add(button_call_1)
        mem = open("media/images.jpg", "rb")
        await bot.send_photo(message.chat.id, photo=mem)

    # question = "Что озночает True в питоне?"
    # answers = ['Ритм', 'Да', 'Один', 'Много']
    # await bot.send_poll(message.chat.id,
    #                     question=question,
    #                     options=answers,
    #                     is_anonymous=False,
    #                     type='quiz',
    #                     correct_option_id=2
    #                     )

@dp.message_handler(commands=['test2'])
async def quinz_1(message: types.Message):
    question = "Что озночает // в питоне?"
    answers = ['Деление без осататка', 'Примножение', 'Falls', 'True']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0
                        )
@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text.isdigit():
        a = int(message.text)
        await message.answer(a ** 2)
    else:
        await message.answer(message.text)

@dp.message_handler()

async def echo_message(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)

