import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from .brain import Brain

TOKEN = os.getenv("TELEGRAM_TOKEN")

brain = Brain()

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    answer = brain.think(text)
    await update.message.reply_text(answer)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Telegram bot is live...")
app.run_polling()
