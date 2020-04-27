"""STAR
Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
the bot for sending and accepting message to and from discord
and communicate with the api
"""
from discord.ext import commands

# setting up the bot
BOT = commands.Bot(command_prefix="")


@BOT.event
async def on_ready():
    """On ready
    """
    print("BOT trainer is ready and in working conditon")

@BOT.command()
async def ping(ctx):
    """To if working without messing it up
    """
    await ctx.send("pong")

@BOT.command()
async def fuck(ctx):
    """To if working without messing it up(vulgar version)
    """
    await ctx.send("you")


# starting the trainer
with open("../../.env", "r") as env:
    BOT.run(env.readlines()[1].split(" ")[-1])
