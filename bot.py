from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config.auth import token

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('FernandoMartinezBot')




# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    logger.info('The command /start has been received')
    update.send_message(
        chat_id=context.message.chat_id,
        text="Hello, I am Fernando Martinez and this is Emotion.  When I first come "
             "to Vice City I feel all lonely, a man on the outside, a foreigner, then I say "
             "Fernando, you like to talk a lot so I get a well paid job on the radio and "
             "begin to make my name as a successful DJ.  Now I'm not so lonely, but I never "
             "forget my roots, I never forget, so I always have a soft spot for Foreigner, "
             "I've been waiting is next."
    )

def help(update, context):
    """Send a message when the command /help is issued."""
    logger.info('The command /help has been received')
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token=token)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
