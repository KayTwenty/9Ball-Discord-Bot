import discord
import datetime
import time
import os
from discord.ext import commands, tasks
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound
from asyncio import sleep
from config import *

client = commands.Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Version 2.3"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9help | 9b"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9gay | 9ship"))
        await sleep(3600)
        await client.change_presence(activity=discord.Streaming(name="WonUpped's Channel", url="http://www.twitch.tv/wonupped"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Staying Alive"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9clear"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Rust"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Ask me Question"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Eleven"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Bonk!!"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("NineBall, your local questioneer!"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9b"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Raw Spaghetti Laser Beam!"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("I Believe In The Sword."))
        await sleep(3600) #Status changer for the bot

def ownercheck(ctx):
    return ctx.message.author.id == 503314109643882529

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

@commands.check(ownercheck)
@client.command(aliases=["refresh"])
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send("9Ball has reloaded the cog!")

@commands.check(ownercheck)
@client.command(aliases=['quit', 'stop', 'exit']) #Shutdown command for Nineball
async def shutdown(ctx):
    await ctx.send("9Ball is shutting down. Please wait...", delete_after=10)
    print("9Ball is shutting down...")
    await logout()

@client.event #Error ignore for MissingPermissions
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        return

@client.event #Error ignore for CommandNotFound
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return

client.run(TOKEN)
