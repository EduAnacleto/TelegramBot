from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
from credentials import get_credentials


token = get_credentials('../Credentials', 'OlhoFinanceiroBot')
bot = Bot(token=token)
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="Random 1-10", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="Random 1-100", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)


@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.answer("Select a range:", reply_markup=keyboard_inline)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.answer("Hello!")
    #await message.reply("Hello!")

@dp.callback_query_handler(text = ["randomvalue_of10", "randomvalue_of100"])
async def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.answer(randint(1, 10))
    if call.data == "randomvalue_of100":
        await call.message.answer(randint(1, 100))
    await call.answer()



executor.start_polling(dp)


