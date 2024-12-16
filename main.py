import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


bot = Bot(token="7754790829:AAGikFJqteL6TGfz3ERcEoglRs4boXZxILc")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Kirill lotin botga hush kelibsiz")
    
@dp.message(ContentType.LOCATION)
async def location_handler(message: types.Message):
    latitude = message.location.latitude  # Latitude
    longitude = message.location.longitude  # Longitude
    await message.answer(f"Sizning joylashuvingiz:\nLatitude: {latitude}\nLongitude: {longitude}")

@dp.message(Command("start"))
async def buttons(message:types.Message):
    menu = types.ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text="asosiy menyu"), KeyboardButton(text="Chiqish"),KeyboardButton(text="asosiy menyu"), KeyboardButton(text="Chiqish")],
            [KeyboardButton(text="Karzinka"), KeyboardButton(text="Bog'lanish")],
            [KeyboardButton(text="asosiy menyu"), KeyboardButton(text="Chiqish")],
            [KeyboardButton(text="Karzinka"), KeyboardButton(text="Bog'lanish")]
        ]

    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())