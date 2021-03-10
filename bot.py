# bot.py
import os
import random

from discord.ext import tasks,commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("logged in as: ",bot.user.name)

@tasks.loop(seconds = 3)
async def get_prize():
    await bot.wait_until_ready()
    


bot.run(TOKEN)