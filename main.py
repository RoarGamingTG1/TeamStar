import os
import random
from pyrogram import Client, filters

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# List of PUBG questions and answers
pubg_data = {
    "What is the full form of PUBG?": "PlayerUnknown's Battlegrounds",
    "When was PUBG first released?": "December 20, 2017",
    "Which company developed PUBG?": "PUBG Corporation",
    "What is the maximum number of players in a PUBG match?": "100",
    "What is the name of the original PUBG map?": "Erangel",
    "Which PUBG map is set in a desert?": "Miramar",
    "What is the name of the smallest PUBG map?": "Sanhok",
    "What is the most popular game mode in PUBG?": "Battle Royale",
    "What is the name of the PUBG currency?": "Battle Points (BP)",
    "What is the main objective in PUBG?": "To be the last player or team standing"
}

# Bot ko create karein
Bot = Client(
    "PUBGQuizBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Start command handler
@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text("Welcome to the PUBG Quiz Bot! Type /quiz to start the quiz.")

# Quiz command handler
@Bot.on_message(filters.command(["quiz"]))
async def quiz(bot, update):
    question = random.choice(list(pubg_data.keys()))
    answer = pubg_data[question]
    await update.reply_text(f"Question: {question}\nAnswer: {answer}")

# Bot ko run karein
Bot.run()
