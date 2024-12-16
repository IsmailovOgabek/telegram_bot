import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


bot = Bot(token="7754790829:AAGikFJqteL6TGfz3ERcEoglRs4boXZxILc")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Kirill lotin botga hush kelibsiz")



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())