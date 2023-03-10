import telebot
import requests
import json
import time
from Settings import TOKEN, OZON_API_TOKEN
from handlers import balance_handler, callback_handler, delivery_handler, \
    products_handler, start_handler, subscribe_handler

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    start_handler.start_handler(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    callback_handler.callback_handler(bot, call)


@bot.message_handler(commands=['products'])
def products(message):
    products_handler.products_handler(bot, message)


@bot.message_handler(commands=['balance'])
def balance(message):
    balance_handler.balance_handler(bot, message)


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    subscribe_handler.subscribe_handler(bot, message)


@bot.message_handler(commands=['delivery'])
def delivery(message):
    delivery_handler.delivery_handler(bot, message)


if __name__ == '__main__':
    bot.polling(none_stop=False)
