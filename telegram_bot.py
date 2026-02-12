import os
import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Get token from environment variable
TOKEN = os.getenv("BOT_TOKEN")


# ---------------- START COMMAND ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Deathroll Game Factory!\n\n"
        "Available commands:\n"
        "/generate_game - Create a new game idea"
    )


# ---------------- GAME GENERATOR ----------------
async def generate_game(update: Update, context: ContextTypes.DEFAULT_TYPE):

    titles = ["Shadow Drift", "Pixel Warzone", "Cyber Rush", "Dragon Arena"]
    genres = ["Battle Royale", "Racing", "RPG", "Action Platformer"]
    styles = ["2D", "3D"]
    monetization = [
        "Ads + In-App Purchases",
        "Premium Version",
        "Reward Ads",
        "Battle Pass System",
    ]
    audience = ["Teens", "Casual Gamers", "Hardcore Players"]
    promotion = [
        "Promote via TikTok short gameplay videos",
        "Run Facebook gaming ads",
        "Create YouTube trailer",
        "Influencer shoutouts",
    ]

    game_idea = f"""
🎮 *New Game Idea Generated!*

🔥 Title: {random.choice(titles)}
🕹 Genre: {random.choice(genres)}
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

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
