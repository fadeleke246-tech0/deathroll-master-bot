
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

from .brain import Brain


brain = Brain()


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    answer = brain.think(text)
    await update.message.reply_text(answer)


def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN environment variable not set")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Telegram bot is live...")
    app.run_polling()


if __name__ == "__main__":
    main()
