import os
import logging
import requests

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = os.environ.get('TELEGRAM_TOKEN')
if not token:
    raise Exception('TELEGRAM_TOKEN is not defined in environment variables')

api_url = os.environ.get('API_URL')
if not api_url:
    raise Exception('API_URL is not defined in environment variables')


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def message(bot, update):
    """Parses the user message and reply."""
    r = requests.get(api_url + '/query', {'message': update.message.text})
    response = r.json()
    update.message.reply_text(response['content'])


def balance(bot, update):
    """Return current balance of the user."""
    r = requests.get(api_url + '/balance')
    response = r.json()
    update.message.reply_text('Your balance is %s' % response['balance'])


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():

    # Connects to telegram
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("balance", balance))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, message))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
