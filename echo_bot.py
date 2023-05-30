# импорт библиотек
import logging
from aiogram import Bot, Dispatcher, executor, types

# здесь токен бота. брать у @BotFather
TOKEN = "<ваш_токен>"

# выод лога в консоль
logging.basicConfig(level=logging.INFO)

# для работы бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# вывод в консоль что бот запущен
async def on_startup(_):
	print('Бот успешно запущен')

# команда старт
@dp.message_handler(commands=['start'])
async def start(message):
	user_id = message.from_user.first_name
	await message.answer(f"Здравствуйте, {user_id}!")
# повторение за пользоватеелем
@dp.message_handler()
async def echo(message):
	await message.answer(message.text)

# цикл
if __name__ == '__main__':
	executor.start_polling(dp, on_startup=on_startup)
