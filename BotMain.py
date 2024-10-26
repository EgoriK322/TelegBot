import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#Token
from Token_For_Teleg import Token
bot = telebot.TeleBot(Token)

#def
from ForBot import pas
from ForBot import gen_emodji
from ForBot import flip_coin
from ForBot import gen_markup


#BotCom    
    
@bot.message_handler(commands=['github'])
def send_hello(message):
    bot.reply_to(message, "Мой код открыт для всех на посмотри https://github.com/EgoriK322/TelegBot/blob/main/BotMain.py")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_pas(message):
    bot.reply_to(message, pas(10))

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")


@bot.message_handler(commands=['dota'])
def send_keys(message):
    bot.send_message(message.chat.id,'Пойдешь в дотан?', reply_markup=gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Пиши сюда https://t.me/EgoriK322")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Нам не о чем разговаривать...")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
    '''
    все интересные команды:
    /coin - для совершения ОЧЕНЬ СЛОЖНОГО выбора просто кинь монетку             
    /password - да как придумать пароль(просто кликни на эту команду)
    /emodji - я уверен кому-то понадобиться рандомный смайлик
    /dota - сюда запрещено нажимать                                         ''')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    



bot.polling()
