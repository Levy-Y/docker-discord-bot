import os
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')

bot.run(os.getenv('TOKEN'))