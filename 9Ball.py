import discord
import random
import datetime
import time
import os
import platform
from random import choice
from discord.ext import commands, tasks
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound
from asyncio import sleep

TOKEN = "NzUwNzg5MjQ3ODkxNTM3OTcy.X0_o-Q.Ts3aldC0AhotqTqdH_QDEo_aAVg"
BOT_PREFIX = '/'

bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')

async def status():
    while True:
        await bot.wait_until_ready()
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("/9help"))
        await sleep(3600)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("Version 2.0"))
        await sleep(500)
        await bot.change_presence(activity=discord.Streaming(name="SHKW Live!", url="http://www.twitch.tv/shockwavesharma"))
        await sleep(500)
        await bot.change_presence(activity=discord.Streaming(name="WonUpped Live!", url="http://www.twitch.tv/wonupped"))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(""))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("GAWR"))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("Gotta Catch 'em All"))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("Ask me Question"))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("SOMEbody once told me"))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("The world is gonna roll me"))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("NineBall, your local questioner!"))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("/9b"))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("Raw Spaghetti Laser Beam!"))
        await sleep(500)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("I Believe In The Sword."))
        await sleep(500) #Status changer for the bot

@bot.event #CMD Screen when Bot starts
async def on_ready():
    users = len(set(bot.get_all_members()))
    ping = (time.monotonic()) / 10000
    print(str(datetime.datetime.now().time()) + " - Connecting to Discord API...")
    print(str(datetime.datetime.now().time()) + " - Connected to Discord API.")
    print(str(datetime.datetime.now().time()) + " - Loading stats and posting to DBL...")
    print(str(datetime.datetime.now().time()) + " - Loading complete!")
    print("Logged in as: " + bot.user.name + "\n")
    print("{} users".format(users))
    print('Servers connected to:')
    for guild in bot.guilds:
        print(guild.name)
bot.loop.create_task(status())

@bot.command(aliases=['9ball', '9Ball', '9b', '9B', 'ball', 'Ball']) #The Main 9Ball command
async def _9ball(ctx, *, question):
    responses = ["As I see it, no.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely",
                "You may rely on it.",
                "Most likely.",
                "Kinda.",
                "Yes.",
                "Signs point to yes.",
                "Yup.",
                "Affirmative.",
                "Don't count on it.",
                "My reply is no",
                "My Sources say no.",
                "very doubtful.",
                "**Yes.**",
                "**No.**",
                "Simp!",
                "Definitely not!",
                "Ask 9Ball once more.",
                "Maybe Not.",
                "Nie.",
                "Negative.",
                "Definitely yes!",
                "I can see it as true.",
                "I can see it as false.",
                "Idk m8... Ask Murphy...",
                "Oh hecc naw!",
                "Definitely."]

    colors = [0x680af5,0x3b21de,0x37c87e,0xe98316,0xee1115,0xed129f,0xed3212,0x1ecbe1,0xf6fff9,0xecbe1,]
    embed=discord.Embed(title="The Extraordinaire 9Ball has Spoken.", color= random.choice(colors))
    embed.set_author(name="Asked by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="Question:", value=question, inline=False)
    embed.add_field(name="Answer:", value=random.choice(responses), inline=False)
    embed.set_footer(text="Commands: /9b | /help")
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def _9help(ctx):
    embed=discord.Embed(title="9Ball Help Commands", color=0x680af5)
    embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="/9ball *Your Question*", value="9Ball answers your desired question.", inline=True)
    embed.add_field(name="/9clear 5, /c", value="9Ball deletes server messages by a selected number.", inline=True)
    embed.add_field(name="/9stats", value="9Ball lists the stats.", inline=False)
    embed.add_field(name="/9about", value="The about page for 9Ball.", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def _9about(ctx):
    embed=discord.Embed(title="Developed By K-20", description="Written in Python Rewrite. It's not an 8Ball but, It's a 9Ball!", color=0x680af5)
    embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/avatars/ae/ae834ef83d652c19e5de5ec93a35c887a575517a_full.jpg")
    embed.add_field(name="Website:", value="https://sites.google.com/view/9-ball-bot/home", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def _9stats(ctx):
    pythonVerison = platform.python_version()
    serverCount = len(bot.guilds)

    embed=discord.Embed(title="9Ball Stats", color=0x680af5)
    embed.set_author(name="Rquested By " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="Python Verison:", value=pythonVerison, inline=True)
    embed.add_field(name="Server Count:", value=serverCount, inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command(aliases=['delete', 'purge', 'c', 'remove']) #Best clear command I've ever done
async def _9clear(ctx, amount: int):
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(title=f"`{amount}` messages were removed.", description="", color=0xff0000)
        await ctx.send(embed=embed, delete_after=3)
    else:
        embed = discord.Embed(title="Error: Permission Denied.", description="Your role must need manage messages to be enabled.", color=0xff0000)
        await ctx.send(embed=embed, delete_after=8)

@bot.event #Error ignore for MissingPermissions
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        raise error





bot.run(TOKEN)
