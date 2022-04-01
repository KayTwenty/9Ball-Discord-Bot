# info.py 
# This is a cog

import discord
import platform

from discord.ext import commands

class info(commands.Cog):
    def __init__(self, client):
        self.client = client
   
    @commands.command(aliases=['Help', 'h']) #The 9Ball help commands...
    async def help(self, ctx):
        embed=discord.Embed(title="9Ball Main Help Commands", color=0x680af5)
        embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="9ball *Your Question*", value="9Ball answers your desired question.", inline=False)
        embed.add_field(name="9clear 5", value="9Ball deletes server messages by a selected number.", inline=False)
        embed.add_field(name="9stats", value="9Ball lists the stats.", inline=False)
        embed.add_field(name="9about", value="The about page for 9Ball.", inline=False)
        embed.add_field(name="9blacklist *UserID*", value="Blacklists any user which is not in server using user's ID", inline=False)
        embed.add_field(name="9join", value="9Ball will join the voice channel", inline=False)
        embed.add_field(name="9dc", value="9Ball will leave the voice channel", inline=False)
        embed.add_field(name="9repeat *text*", value="9Ball will repeat whatever you've said", inline=False)
        embed.set_footer(text="Commands: 9help2 for page 2")
        await ctx.reply(embed=embed)

    @commands.command(aliases=['funhelp', 'fun']) #Fun 9ball commands
    async def help2(self, ctx):
        embed=discord.Embed(title="9Ball Fun Help Commands", color=0x680af5)
        embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="9cookie @user", value="Gives cookie to the selected user.", inline=False)
        embed.add_field(name="9bonk @user", value="9Ball bonks the selected user.", inline=False)
        embed.add_field(name="9hug @user", value="Gives a hug to the selected user.", inline=False)
        embed.add_field(name="9kiss @user", value="Kisses user (Covid free).", inline=False)
        embed.add_field(name="9fistbump @user", value="fistbump user.", inline=False)
        embed.add_field(name="9frick @user", value="Oh yeah bb!!.", inline=False)
        embed.add_field(name="9donut @user", value="Gives donut to user.", inline=False)
        embed.add_field(name="9ship @user @user", value="9Ball will ship two selected users.", inline=False)
        embed.add_field(name="9gay @user", value="9Ball will determine the gay percent on the selected user.", inline=False)
        embed.set_footer(text="Commands: 9help for page 1")
        await ctx.reply(embed=embed)

    @commands.command(aliases=['About', 'creator']) #The about page for 9Ball
    async def about(self, ctx):
        embed=discord.Embed(title="Developed By K-20", description="Written in Python Rewrite. It's not an 8Ball but, It's a 9Ball!", color=0x680af5)
        embed.set_author(name="Requested by: " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/avatars/ae/ae834ef83d652c19e5de5ec93a35c887a575517a_full.jpg")
        embed.add_field(name="Website:", value="https://sites.google.com/view/9-ball-bot/home", inline=False)
        embed.add_field(name="Invite Link:", value="https://tinyurl.com/2e8wn5f2", inline=False)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['Stats', 'stat']) #Devs stats for the current 9Ball
    async def stats(self, ctx):
        pythonVerison = platform.python_version()
        serverCount = len(self.client.guilds)
        embed=discord.Embed(title="9Ball Stats", color=0x680af5)
        embed.set_author(name="Rquested By " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Python Verison:", value=pythonVerison, inline=True)
        embed.add_field(name="Server Count:", value=serverCount, inline=True)
        await ctx.reply(embed=embed)
    
def setup(client):
    client.add_cog(info(client))