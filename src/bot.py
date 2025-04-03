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

async def load_commands():
    for filename in os.listdir("./src/command"):
        if filename.endswith(".py"):
            await bot.load_extension(f"command.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"✅ Bot connectado como {bot.user}")
    print("----------------------------------")
    await load_commands()

bot.run(TOKEN)