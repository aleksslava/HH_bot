import requests
from requests_oauthlib import OAuth2Session
import telebot

client_id = 'OG7PSK82HJVOKILRPCAL33JP83746S4V16V891EJGG72HS0RPPBI2GL2OTGJ3TDO'
client_secret = 'M5GHCB3T5B6S52VGJGQ30LTDMDMOHOI2HMP0CH35R2FHJK7T562J89SDM76A8U6E'
hh_token = 'OFS49QN68T2UJLG4THTKE5IT49IDMSQKB52C5N7NV6LTFVQ2RG8TVHQDL1A11004'

tg_token = '5683462995:AAFEfUkWKOBZvkCPOYtrkC1q2UvwtqvBgN8'

bot = telebot.TeleBot(tg_token)
params = {
    'response_type': 'code',
    'client_id': client_id,
}
url = 'https://hh.ru/oauth/authorize'
oauth = OAuth2Session(client_id=client_id)
authorization_url, state = oauth.authorization_url(url)
text = f'Перейдите по ссылке и авторизуйтесь: {authorization_url}'

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, text)
    bot.send_message(m.chat.id, 'Скопируйте в чат код из строки запроса')

@bot.message_handler(func=lambda m: True)
def get_token(m):
    code, state_inc = m.text.split('&')
    _, code = code.split('=')
    _, state_inc = state_inc.split('=')
    if state == state_inc:
        global auth_code
        auth_code = code


    else:
        bot.send_message(m.chat.id, 'Введен неверный код')


bot.infinity_polling()