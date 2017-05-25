# -*- coding: utf-8 -*-

import telebot # librería para usar el bot
import os



bot = telebot.TeleBot(os.environ["TOKENBOT"])

@bot.message_handler(commands=['start'])
def enviar_bienvenida(message):
    """Función de bienvenida del canal. """
    bot.reply_to(message, "Bievenid@")

@bot.message_handler(commands=['Francia'])
def enviar_actividades(m):
    """Función que envia las actividades de la semana al usuario. """
    cid = m.chat.id # Obtenemos la id del usuario.

    bot.send_message(cid, "La capital de Francia es París.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop=True) # Le indicamos que nunca termine de funcionar.
