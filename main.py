import telebot
from telebot import types
import requests

bot = telebot.TeleBot('5667334128:AAGw1q7ZWNpfUou7MSV5OhLVh5N2m1Q55nE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Короткие ссылки')
    item2 = types.KeyboardButton('Курс валют')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup=markup)


bot.infinity_polling()
