import telebot
from dotenv import load_dotenv
import os
import utils


load_dotenv()
my_tg_token = os.getenv("TOKEN")

bot = telebot.TeleBot(my_tg_token)
print("Бот запущено!!")


@bot.message_handler(commands=["coin"])
def coin_message(message):
    result = utils.flip_coin()
    bot.send_message(message.chat.id,
                     f"Бот підкинув монетку, випало - {result}")


@bot.message_handler(commands=["dice"])
def dice_message(message):
    result = utils.roll_dice()
    bot.send_message(message.chat.id,
                     f"Бот підкинув кубик. На ньому випало - {result}")



@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Бот запущено!")

@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, "Чим тобі допомгти?!")

@bot.message_handler(content_types=["text"])
def text_message(message):
    mytext = message.text
    if mytext == "Привіт":
        bot.send_message(message.chat.id, "І тобі привіт юзер!")
    elif mytext == "Папа":
        bot.send_message(message.chat.id, "І тобі папа юзер!")
    else:
        bot.send_message(message.chat.id, "Я тебе не зрозумів!")




bot.infinity_polling()