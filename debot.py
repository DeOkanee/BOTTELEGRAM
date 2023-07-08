import openai
import asyncio
import telebot
import speech_recognition as sr
import os

# Masukkan API OPENAI
openai.api_key = "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"
bot = telebot.TeleBot('6078660342:AAFxkjXMH93T5QqUEONMLnyQlzyhV4lVALI')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hallo, Saya Google tapi versi duanya, Silakan tanya apa aja....
Waktu DEBOT menjawab akan menyesuaikan dari pertanyaan anda 😃🤔

# /menu
# /about
""")


@bot.message_handler(commands=['menu'])
def send_welcome(message):
    bot.reply_to(message, """\
Jangan lupa mampir kak ⬇️
"https://profil-deoka.vercel.app/"
""")


@bot.message_handler(commands=['about'])
def send_welcome(message):
    bot.reply_to(message, """\
Ayo manfaatkan aplikasi telegram untuk kepentingan positif,
dan jadikan "TANYADEBOT" sebagai jawaban dari pertanyaanmu"
""")


@bot.message_handler(func=lambda message: True)
def process_message(message):
    if message.voice:
        voice_file_info = bot.get_file(message.voice.file_id)
        voice_file = bot.download_file(voice_file_info.file_path)
        
        # Simpan file suara sementara
        voice_filename = 'voice_message.ogg'
        with open(voice_filename, 'wb') as f:
            f.write(voice_file)
        
        # Konversi suara menjadi teks menggunakan library SpeechRecognition
        r = sr.Recognizer()
        with sr.AudioFile(voice_filename) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
        
        # Hapus file suara sementara
        os.remove(voice_filename)
        
        # Gunakan teks yang dihasilkan dari suara untuk mendapatkan jawaban dari AI
        response = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0, max_tokens=1000)
        answer = response['choices'][0]['text']
        
        # Kirim jawaban dalam bentuk pesan suara
        bot.send_chat_action(message.chat.id, 'record_audio')
        bot.send_voice(message.chat.id, answer)
    else:
        response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
        bot.reply_to(message, response['choices'][0]['text'])


bot.polling()
