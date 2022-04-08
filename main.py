import discord
import os
import json
import datetime
import time

from discord.ext import commands
from asyncio import sleep
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound

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
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

async def status(): #Status changer for the bot
    while True:
        await client.wait_until_ready()
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9Ball has voice support"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Version 2.7"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9help | 9b"))
        await sleep(3600)
        await client.change_presence(activity=discord.Streaming(name="Nerd", url="https://www.twitch.tv/sodapoppin"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("..."))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9clear"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Check out Mango-Bot!"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Ask me Question"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9meme"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("League of Leg"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("NineBall, your local questioneer!"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9b"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Raw Spaghetti Laser Beam!"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Summer is ending"))
        await sleep(3600)

'  The start screen  '
@client.event #CMD Screen when Bot starts
async def on_ready():
    users = len(set(client.get_all_members()))
    ping = (time.monotonic()) / 10000
    print('-----------------------------------------------------------------------------')
    print(str(datetime.datetime.now().time()) + " - Connecting to Discord API...")
    print(str(datetime.datetime.now().time()) + " - Connected to Discord API.")
    print(str(datetime.datetime.now().time()) + " - Loading stats and posting to DBL...")
    print(str(datetime.datetime.now().time()) + " - Loading complete!")
    print("Logged in as: " + client.user.name + "\n")
    print("{} users".format(users))
    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)
    print('------------------------------------------------------------------------------')
client.loop.create_task(status())


' The Errorhandling  '
@client.event #Error ignore for MissingPermissions
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        return

'  The Errorhandling  '
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.reply(f">>> **I just found an error!**\n{error}")  # Errormessage


client.run(TOKEN)
