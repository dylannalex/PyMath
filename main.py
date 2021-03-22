import os
import sys
import logging
import text as txt
import responses as res
import telegram
from telegram.ext import Filters
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler

# Logging configuration
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

# Enviroment constants:
TOKEN = os.getenv('TOKEN')
MODE = os.getenv('MODE')

# Other constants:
SPECIAL_CHARS = ('_', '*', '[', ']', '(',
                 ')', '~', '`', '>', '#',
                 '+', '-', '=', '|', '{',
                 '}', '.', '!')

# detect mode
if MODE == 'test':
    # Local access
    def run(updater):
        updater.start_polling()
        print('PyMath Bot ready')
        updater.idle()  # End bot with Ctrl + C

elif MODE == 'deploy':
    # Heroku access
    def run(updater):
        PORT = int(os.environ.get('PORT', '8443'))
        HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME')
        updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(
            f'https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}')

else:
    logger.info('"MODE" not specified')
    sys.exit()


# Commands
def start(update, context) -> None:
    name = update.effective_user['first_name']
    user_id = update.effective_user['id']

    logger.info(f'[{user_id}] {name} has initialized PyMath bot')

    # Send msg to user
    context.bot.sendMessage(
        chat_id=user_id,
        parse_mode='MarkdownV2',
        text=f"Hi {name}, I'm *PyMath*\\. Type /help to see what I can do for you\\!")


def help(update, context) -> None:
    user_id = update.effective_user['id']
    context.bot.sendMessage(
        chat_id=user_id,
        parse_mode='MarkdownV2',
        disable_web_page_preview=True,
        text=txt.HELP)


def handle_message(update, context) -> None:

    command = str(update.message.text).lower().strip()
    user_id = update.effective_user['id']

    if command == 'help':
        return help(update, context)

    if command == 'vectors':
        return vectors(update, context)

    if command == 'plane' or command == 'planes':
        return plane(update, context)

    if command == 'matrices':
        return matrices(update, context)

    try:
        output = res.response(command)
        # Replace special characters in output:
        valid_output = ''
        for i in output:
            if i in SPECIAL_CHARS:
                valid_output += f'\\{i}'
            else:
                valid_output += i

        # Send output to user
        context.bot.sendMessage(
            chat_id=user_id,
            parse_mode='MarkdownV2',
            text=valid_output)

    except Exception as error:
        logger.warning(
            f'PyMath could not answer to "{command}" due to: {error}')

        # Warn user
        context.bot.sendMessage(
            chat_id=user_id,
            parse_mode='MarkdownV2',
            text=r'Sorry\, I can\'t answer that\!')


# Linear algebra commands:
def vectors(update, context) -> None:
    context.bot.sendMessage(
        chat_id=update.effective_user['id'],
        parse_mode='MarkdownV2',
        text=txt.VECTOR_COMMANDS)


def plane(update, context) -> None:
    context.bot.sendMessage(
        chat_id=update.effective_user['id'],
        parse_mode='MarkdownV2',
        text=txt.PLANES_COMMANDS)


def matrices(update, context) -> None:
    context.bot.sendMessage(
        chat_id=update.effective_user['id'],
        parse_mode='MarkdownV2',
        text=txt.MATRICES_COMMANDS)


# Chemistry commands:
def atoms(update, context) -> None:
    context.bot.sendMessage(
        chat_id=update.effective_user['id'],
        parse_mode='MarkdownV2',
        text=txt.ATOMS_COMMANDS)


def main() -> None:
    bot = telegram.Bot(token=TOKEN)

    # Sincronize updater with bot
    updater = Updater(bot.token, use_context=True)

    # Create dispatcher (to recieve msgs and organize traffic)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    # Linear algebra commands
    dp.add_handler(CommandHandler('vectors', vectors))
    dp.add_handler(CommandHandler('plane', plane))
    dp.add_handler(CommandHandler('matrices', matrices))

    # Chemistry commands
    dp.add_handler(CommandHandler('atoms', atoms))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    run(updater)


if __name__ == '__main__':
    main()
