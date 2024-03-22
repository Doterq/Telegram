import config
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot


API_TOKEN = config.TG_TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=['info'])
def send_info(message):
    print(message)
    bot.reply_to(message,"\
Здесь есть информация о боте\
" )
    
from random import choice

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    print(message)
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(coin)




# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

#@bot.big_file_id(comands =["mem"])
#def memr_photo(shutka):
#    print(shutka)

1