''' PYTHON-TELEGRAM_BOT '''

# for debugging
import logging

# Bot Commands
from telegram.ext import CommandHandler

# To establish the connection
from telegram.ext import Updater

# To receive messages
from telegram.ext import MessageHandler, Filters

# Bot Token 
BOT_TOKEN = "1105791347:AAG2x9MfHW5JwJcW3s4r5jkAXKnCQX0wi7I"

# Updater = Make the connection with the bot
updater = Updater(token=BOT_TOKEN, use_context=True)

# Send/received data from message
dispatcher = updater.dispatcher

# for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Message to send
start_text = "I'm a bot, please talk to me!"

# Start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text)



def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def unknown(update, context):
    print(f"context: {}", context)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


# Start Command
start_handler = CommandHandler('start', start)
# Message Handler
echo_handler = MessageHandler(Filters.text, echo)
# Unknow command handler
unknown_handler = MessageHandler(Filters.command, unknown)

# Sending the message
# dispatcher.add_handler(start_handler)

# dispatcher.add_handler(unknown_handler)

dispatcher.add_handler(echo_handler, unknown_handler, start_handler)

updater.start_polling()