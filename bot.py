from time import time
from datetime import datetime

import telebot
#documentation
#https://pytba.readthedocs.io/en/latest/index.html



API_TOKEN = 'telegram bot token'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am A Bot.
I am here to send you notifications about some things idk yet\
""")

#if user sends hello message to bot it will reply with hello message
@bot.message_handler(func=lambda message: message.text == "hello")
def send_welcome(message):
    bot.reply_to(message, "hello")



now = datetime.now()

current_time = now.strftime("%H:%M:%S")

#if user ask time to bot it will reply with time
@bot.message_handler(func=lambda message: message.text == "time")
def send_welcome(message):
    bot.reply_to(message, current_time)





bot.infinity_polling()