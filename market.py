import telebot
import mysql.connector
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot('5361386002:AAGWD2BtOO7fwsQ84I1tiopAgwuTzIPNO8A')


class Markets:
    def start_command(self, message):
        keyboard = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text="Новый товал", callback_data="new_p")
        button2 = InlineKeyboardButton(text="Мои товары", callback_data="my_p")
        keyboard.add(button1, button2)
        bot.send_message(message.chat.id, 'Здрасвтвуйте, хотители вы:', reply_markup = keyboard)
        
