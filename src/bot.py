import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connectado como {bot.user}")
    print("----------------------------------")

bot.run(TOKEN)