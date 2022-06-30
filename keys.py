import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)
from buttons import knopka,  knop



def main_menu_keyboard():
    keyboard = (
        [
            [telegram.KeyboardButton(knop[0])] 
        ]
    )
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def vacancies():
    keyboard = (
        [
            [telegram.KeyboardButton(knopka[0])],
            [telegram.KeyboardButton(knopka[1])],
            [telegram.KeyboardButton(knopka[2])], 
        ]
    )
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )