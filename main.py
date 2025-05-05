import logging
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Welcome to Squonk Radio V0.4.3!\nUse /setup to link your group.")

@dp.message_handler(commands=['setup'])
async def setup_command(message: types.Message):
    await message.reply("📩 Send me `GroupID: <your_group_id>` to link your group.", parse_mode='Markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
