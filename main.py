import requests
import telebot
from datetime import datetime
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)


def get_re(): # connection test, if have connection just delete this def
    reg = requests.get('https://yobit.net/api/3/ticker/eth_usd')
    req2 = requests.get('https://yobit.net/api/3/ticker/doge_usdt')
    req3 = requests.get('https://yobit.net/api/3/ticker/btc_usdt')
    req4 = requests.get('https://yobit.net/api/3/ticker/dash_usd')
    req5 = requests.get('https://yobit.net/api/3/ticker/ltc_usd')

    respon = reg.json()
    respon2 = req2.json()
    respon3 = req3.json()
    respon4 = req4.json()
    respon5 = req5.json()

    sellprice = respon['eth_usd']['sell']
    sellprice2 = respon2['doge_usdt']['sell']
    sellprice3 = respon3['btc_usdt']['sell']
    sellprice4 = respon4['dash_usd']['sell']
    sellprice5 = respon5['ltc_usd']['sell']

    print(f"""{datetime.now().strftime('%d-%m-%Y %H:%M')}\nSell price ETH-USD: {sellprice}\nSell price DOGE-USDT: {sellprice2}
    Sell price BTC_USDT: {sellprice3}\nSell price DASH_USD: {sellprice4}\nSell price LTC_USD: {sellprice5}"""
    )



@bot.message_handler(commands=['start'])
def send_welc(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('ETH Price')
    item2 = types.KeyboardButton('DOGE Price')
    item3 = types.KeyboardButton('BTC-USDT Price')
    item4 = types.KeyboardButton('DASH Price')
    item5 = types.KeyboardButton('LTC Price')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id,
                     'Hello there! Please choose what TOKEN price do you want to know.', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def price_tok(message):
    if (message.text == 'ETH Price'):
        try:
            reg = requests.get('https://yobit.net/api/3/ticker/eth_usd')
            respon = reg.json()
            sellprice = respon['eth_usd']['sell']
            bot.send_message(message.chat.id,
                             f"{datetime.now().strftime('%d-%m-%Y %H:%M')}\nSell price ETH-USD:{sellprice}")
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Sorry! It's not working!")
    elif (message.text == 'DOGE Price'):
        try:
            req2 = requests.get('https://yobit.net/api/3/ticker/doge_usdt')
            respon2 = req2.json()
            sellprice2 = respon2['doge_usdt']['sell']
            bot.send_message(message.chat.id,
                         f"{datetime.now().strftime('%d-%m-%Y %H:%M')}\nSell price DOGE-USDT:{sellprice2}")
        except Exception as ex1:
            print(ex1)
            bot.send_message(message.chat.id, "Sorry! It's not working!")
    elif (message.text == 'BTC-USDT Price'):
        try:
            req3 = requests.get('https://yobit.net/api/3/ticker/btc_usdt')
            respon3 = req3.json()
            sellprice3 = respon3['btc_usdt']['sell']
            bot.send_message(message.chat.id,
                             f"{datetime.now().strftime('%d-%m-%Y %H:%M')}\nSell price BTC-USDT: {sellprice3}")
        except Exception as ex2:
            print(ex2)
            bot.send_message(message.chat.id, "Sorry! It's not working!")
    elif (message.text == 'DASH Price'):
        try:
            req4 = requests.get('https://yobit.net/api/3/ticker/dash_usd')
            respon4 = req4.json()
            sellprice4 = respon4['dash_usd']['sell']
            bot.send_message(message.chat.id,
                             f"{datetime.now().strftime('%d-%m-%Y %H:%M')}\nSell price DASH: {sellprice4}")
        except Exception as ex3:
            print(ex3)
            bot.send_message(message.chat.id, "Sorry! It's not working!")
    elif(message.text == 'LTC Price'):
        try:
            req5 = requests.get('https://yobit.net/api/3/ticker/ltc_usd')
            respon5 = req5.json()
            sellprice5 = respon5['ltc_usd']['sell']
            bot.send_message(message.chat.id,
                             f"{datetime.now().strftime('%d-%m-%Y %H:%M')}\nSell price LTC: {sellprice5}")
        except Exception as ex4:
            print(ex4)
            bot.send_message(message.chat.id, "Sorry! It's not working!")
    else:
        bot.send_message(message.chat.id, 'Please choose what you do know:')




bot.infinity_polling()

if __name__ == '__main__':
    get_re()
