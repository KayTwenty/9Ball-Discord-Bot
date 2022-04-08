import discord
import random
 
from discord.ext import commands
from utils.reference import *

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True) #Cookie Command
    async def cookie(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person has gave you a cookie!", description="**{1}** gave a cookie to **{0}**! :cookie:".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Cookie sent by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(cookieurl))
        embed.set_footer(text="Command: 9cookie @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True) #Cookies Command
    async def cookies(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person has gave you a bunch of cookies", description="**{1}** gave cookies to **{0}**! :cookie:".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Cookies sent by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(cookiesurl))
        embed.set_footer(text="Command: 9cookies @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True) #Bonk Command
    async def bonk(self, ctx, member: discord.Member):
        embed = discord.Embed(title="**Bonk!**", description="**{1}** Bonked **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Bonked by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(bonkurl))
        embed.set_footer(text="Command: 9bonk @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True) #Hug Command
    async def hug(self, ctx, member: discord.Member):
        embed = discord.Embed(title="Sending...", description="**{1}** hugs **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Hugged by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(hugurl))
        embed.set_footer(text="Command: 9hug @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True) #Kiss Command
    async def kiss(self, ctx, member: discord.Member):
        embed = discord.Embed(title="*This person gave you a suprise!*", description="**{1}** kissed **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Kissed by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(kissurl))
        embed.set_footer(text="Command: 9kiss @user | (Covid Free)")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True, aliases=['fb', 'bump']) #Fistbump Command
    async def fistbump(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person gave you a fistbump ;)", description="**{1}** fistbumped **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Fistbumped by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(fistbumpurl))
        embed.set_footer(text="Command: 9fistbump @user | 9fb @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True, aliases=['sex', 'fuck']) #Frick Command
    async def frick(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person had sex with you ;)", description="**{1}** fucked **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Fricked by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(frickurl))
        embed.set_footer(text="Command: 9frick @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True, aliases=['do', 'donu']) #Donut Command
    async def donut(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person gave you donut!", description="**{1}** gave donut to **{0}** :doughnut:".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Donut sent by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(donuturl))
        embed.set_footer(text="Command: 9donut @user | 9do @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(client):
    client.add_cog(fun(client))
