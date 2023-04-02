
# ? Bot Username: ChatMate123Bot
# ? Bot Name: ChatMate

import Constants as my_keys
import Responses as R

from telegram.ext import *

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('If you need help, Google it!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.respond_to_message(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(my_keys.API_KEY, use_context=True)

    dp = updater.dispatcher

    # Adding handlers
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    # Running the bot
    updater.start_polling()
    updater.idle()  # This will keep the bot running until you press Ctrl+C


if __name__ == '__main__':
    main()
