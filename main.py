import logging

from aiogram import Bot, Dispatcher, types

from aiogram.utils import executor

from googletrans import Translator
translator = Translator()

API_TOKEN = '6967286418:AAFOAwZGmwYgy1z0CtXYAbWI07TujleUV4s'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Salom. Men Transliterate bot")
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("Bu bot istalgan tildagi so'zni ingliz tiliga tarjima qiladi.")
@dp.message_handler()
async def tarjima(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split())>0:
        dest = 'uz' if lang == 'en' else 'en'
    if (message.text.split())== message.text:
        
        await message.answer(translator.translate(message.text, dest).text)
    
if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
