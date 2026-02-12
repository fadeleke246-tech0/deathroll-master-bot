import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN not set")


def start(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 Bot is live on Render!")


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    print("Bot started successfully")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
