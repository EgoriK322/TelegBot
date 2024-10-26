import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def pas(leng):

    abc="abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password=""

    for i in range(leng):
        num = random.randint(0, len(abc)-1)
        password += abc[num]

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)



def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
    
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                InlineKeyboardButton("No", callback_data="cb_no"))
    return markup
