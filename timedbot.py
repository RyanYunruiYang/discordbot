import os
import discord
from discord.ext import tasks, commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")

channel_ID = 819053433628655616

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("Logged in as:", bot.user.name, "------")
    channel = bot.get_channel(channel_ID)
    print("Channel is:",channel)
    sendToRyan.start()

@tasks.loop(seconds=60*5)
async def sendToRyan():
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_ID)
    print("Channel is:")
    print(channel) #Prints None
    await channel.send('<@&819055576528715776> Log your work hours')


@sendToRyan.before_loop
async def before ():
    print("Before done.")


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)


bot.run(TOKEN)