import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot

# Masukkan API OPENAI & BOT TELEGRAM
openai.api_key = "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"
bot = AsyncTeleBot('6615579760:AAFXYv12JQ8e-m8f2BccTorBm6_DFXqtsXE')

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hallo, Saya Google tapi versi keduanya, Silakan tanya apa aja....
Waktu DEBOT menjawab akan menyesuaikan dari pertanyaan anda 😃🤔

# /menu
# /about
\
""")

@bot.message_handler(commands=['menu'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Jangan lupa mampir kak ⬇️
"https://profil-deoka.vercel.app/"
\
""")

@bot.message_handler(commands=['about'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Ayo manfaatkan aplikasi telegram untuk kepentingan positif,
dan jadikan "TANYADEBOT" sebagai jawaban dari pertanyaanmu"
\
""")

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    # Kirim pesan "Sedang mengetik"
    await bot.send_chat_action(message.chat.id, 'typing')
    
    # Dapatkan jawaban dari OpenAI
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
    
    # Kirim jawaban
    await bot.send_message(message.chat.id, response['choices'][0]['text'])

asyncio.run(bot.polling())
