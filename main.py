import discord
import os
import json

from discord.ext import commands
from asyncio import sleep
from discord.ext.commands import MissingPermissions

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "9"}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

TOKEN = configData["Token"]
BOT_PREFIX = configData["Prefix"]

client = commands.Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# CMD Screen when Bot starts
@client.event
async def on_ready():
    print("Logged in as: " + client.user.name + "\n")
    print("Servers connected to:")
    for guild in client.guilds:
        print(guild.name)


# Error ignore for MissingPermissions
@client.event
async def on_command_error(error):
    if isinstance(error, MissingPermissions):
        return


# Errormessage
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.reply(f">>> **I just found an error!**\n{error}")


try:
    client.run(TOKEN)
except Exception as e:
    print(f"Error when logging in: {e}")
