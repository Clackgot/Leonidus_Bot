import telebot

bot = telebot.TeleBot("1108888413:AAE5Jxnhdzyk5JR6YKxR7KKMemdD1IeSDGY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()