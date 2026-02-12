import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get bot token from environment variable
TOKEN = os.getenv("BOT_TOKEN")


# ---------------- START COMMAND ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Deathroll Game Factory!\n\n"
        "Available commands:\n"
        "/generate_game - Create a new random game idea\n"
        "/about - About this bot"
    )


# ---------------- ABOUT COMMAND ----------------
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Deathroll Game Factory Bot\n"
        "This bot generates random 2D & 3D game ideas\n"
        "with monetization and promotion strategies."
    )


# ---------------- GAME GENERATOR ----------------
async def generate_game(update: Update, context: ContextTypes.DEFAULT_TYPE):

    titles = ["Shadow Drift", "Pixel Warzone", "Cyber Rush", "Dragon Arena", "Neon Escape"]
    genres = ["Battle Royale", "Racing", "RPG", "Action Platformer", "Survival"]
    styles = ["2D", "3D"]
    monetization = [
        "Ads + In-App Purchases",
        "Premium Version",
        "Reward Ads",
        "Battle Pass System"
    ]
    audience = ["Teens", "Casual Gamers", "Hardcore Players", "Mobile Players"]
    promotion = [
        "Promote via TikTok short gameplay videos",
        "Run Facebook gaming ads",
        "Create YouTube trailer",
        "Influencer shoutouts",
        "Launch on gaming forums"
    ]

    game_idea = f"""
🎮 *New Game Idea Generated!*

🔥 Title: {random.choice(titles)}
🎯 Genre: {random.choice(genres)}
🎨 Style: {random.choice(styles)}
👥 Target Audience: {random.choice(audience)}
💰 Monetization: {random.choice(monetization)}

📢 Promotion Strategy:
- {random.choice(promotion)}
"""

    await update.message.reply_text(game_idea, parse_mode="Markdown")


# ---------------- MAIN FUNCTION ----------------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate_game", generate_game))
    app.add_handler(CommandHandler("about", about))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
