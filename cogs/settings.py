import discord
import os
import platform
import datetime
from datetime import datetime
from discord.ext import commands

class settings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['About', 'creator']) #The about page for 9Ball
    async def about(self, ctx):
        embed=discord.Embed(title="Developed By K-20", description="Written in Python Rewrite. It's not an 8Ball but, It's a 9Ball!", color=0x680af5)
        embed.set_author(name="Requested by: " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/avatars/ae/ae834ef83d652c19e5de5ec93a35c887a575517a_full.jpg")
        embed.add_field(name="Website:", value="https://sites.google.com/view/9-ball-bot/home", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['Stats', 'stat']) #Devs stats for the current 9Ball
    async def stats(self, ctx):
        pythonVerison = platform.python_version()
        serverCount = len(client.guilds)

        embed=discord.Embed(title="9Ball Stats", color=0x680af5)
        embed.set_author(name="Rquested By " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Python Verison:", value=pythonVerison, inline=True)
        embed.add_field(name="Server Count:", value=serverCount, inline=True)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(aliases=['delete', 'purge', 'c', 'remove']) #Best clear command I've ever done
    async def clear(self, ctx, amount: int):
        if ctx.message.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(title=f"`{amount}` messages were removed.", description="", color=0xff0000)
            await ctx.send(embed=embed, delete_after=3)
        else:
            embed = discord.Embed(title="Error: Permission Denied.", description="Your role must need manage messages to be enabled.", color=0xff0000)
            await ctx.send(embed=embed, delete_after=8)

def setup(client):
    client.add_cog(settings(client))
