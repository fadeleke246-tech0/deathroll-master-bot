import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# ---------- START COMMAND ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Deathroll Game Factory!\n\n"
        "Available commands:\n"
        "/generate_game - Create a new game idea"
    )

# ---------- GAME GENERATOR ----------
async def generate_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    titles = ["Shadow Drift", "Pixel Warriors", "Neon Clash", "Zombie Arena", "Cyber Runner"]
    genres = ["Battle Royale", "Racing", "Adventure", "Horror", "Arcade Shooter"]
    styles = ["2D", "3D"]
    monetization = ["Ads + In-App Purchases", "Premium Paid Game", "Subscription Model", "Rewarded Ads"]
    audience = ["Teens", "Casual Gamers", "Hardcore Players", "Mobile Gamers"]
    promotion = [
        "Promote via TikTok short gameplay clips",
        "Run Facebook gaming ads",
        "Create YouTube trailer",
        "Influencer shoutouts",
        "Telegram gaming communities"
    ]

    game_idea = f"""
🎮 *Game Title:* {random.choice(titles)}

🕹 *Genre:* {random.choice(genres)}
🌍 *Style:* {random.choice(styles)}

💰 *Monetization:* {random.choice(monetization)}
🎯 *Target Audience:* {random.choice(audience)}

📢 *Promotion Strategy:* {random.choice(promotion)}
"""

    await update.message.reply_text(game_idea, parse_mode="Markdown")

# ---------- MAIN ----------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate_game", generate_game))

    print("🤖 Telegram bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
