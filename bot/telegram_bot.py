import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

 from .brain import Brain # make sure brain.py exists

# create brain instance
brain = Brain()


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text
    answer = brain.think(text)

    await update.message.reply_text(answer)


if __name__ == "__main__":
    TOKEN = os.getenv("TELEGRAM_TOKEN")

    if not TOKEN:
        raise ValueError("TELEGRAM_TOKEN not found in environment variables")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
    )

    print("🤖 Telegram bot is live...")
    app.run_polling()
