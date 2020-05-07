"""STAR
Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
the bot for sending and accepting message to and from discord
and communicate with the api
"""
import requests
from discord import Client


class MyClient(Client):
    """the bot client class"""

    def __init__(self):
        super().__init__()
        self.params = {}

    async def on_ready(self):
        """on bot ready"""
        print("Logged on as", self.user)

    async def on_message(self, message):
        """All the logic is here"""

        # make things easier
        content = message.content.replace("  ", " ").replace("  ", " ")
        send = message.channel.send

        # coz you don't wanna start an infinite loop
        if message.author == self.user:
            return
        words = content.split(" ")

        # to check if bot is up
        if content == "ping":
            await send("pong")
            return
        if content == "fuck":
            await send("you")
            return

        # setting parameters
        if words[0] == "set":
            if len(words) == 4:
                if words[2] == "=" or words[2] == "as" or words[2] == "to":
                    self.params[words[1]] = words[3]
            elif len(words) == 2:
                (param, value) = words[1].split("=")
                self.params[param] = value
                # params = set_param(param, value)
            else:
                await send("well, that did not work")
            return

        # getting parameters
        if words[0] == "show":
            if len(words) > 1:
                for word in words[1:]:
                    if word in self.params:
                        await send(word, "=", self.params[word])
                    else:
                        await send(word + "has not been set")
            else:
                for param, value in self.params.items():
                    await send(param + " = " + value)
            return

        # removing parameters
        if words[0] == "rm" or words[0] == "remove":
            for word in words[1:]:
                if word in self.params:
                    self.params.pop(words[1])
                else:
                    await send(word, "was not in the list of parameters")
            return

        # remove all parameters
        if words == ["clear"]:
            self.params.clear()
            await send("parameters have been cleared")


CLIENT = MyClient()
with open("../../.env", "r") as env:
    CLIENT.run(env.readlines()[1].split(" ")[-1])


# setting up the bot
# BOT = commands.Bot(command_prefix="")


# @BOT.event
# async def on_ready():
#     """On ready
#     """
#     print("BOT trainer is ready and in working conditon")


# @BOT.command()
# async def ping(ctx):
#     """To if working without messing it up
#     """
#     await ctx.send("pong")


# @BOT.command()
# async def fuck(ctx):
#     """To if working without messing it up(vulgar version)
#     """
#     await ctx.send("you")


# @BOT.command()
# async def run(ctx):
#     """TO run the command from discord via the bot
#     """
#     await ctx.send("starting... 🤔")
#     params = {
#         "f": "sqrt(4 - xs**2)",
#         "a": "0",
#         "b": "2",
#         "c": "0",
#         "d": "2",
#         "size": "1000",
#     }
#     req = requests.put("http://localhost:5000", json=params)
#     await ctx.send(f"process has started:\n{req.text}")


# # starting the trainer
# with open("../../.env", "r") as env:
#     BOT.run(env.readlines()[1].split(" ")[-1])
