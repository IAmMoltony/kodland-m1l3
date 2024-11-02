#!/usr/bin/python3

import random
import telebot
from m1l3_botlogic import generate_password
    
bot = telebot.TeleBot("insert ur token here")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    bot.reply_to(message, random.choice("орёл", "решка"))

@bot.message_handler(commands=['passwd'])
def send_passwd(message):
    bot.reply_to(message, generate_password(10))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
print("bot started ok")
bot.polling()
