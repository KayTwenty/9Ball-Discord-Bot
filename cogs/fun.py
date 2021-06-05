import discord
import os
import sys
import datetime
from datetime import datetime
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True) #Cookie Command
    async def cookie(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person has gave you a cookie!", description="**{1}** gave a cookie to **{0}**! :cookie:".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Cookie sent by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url="https://media1.tenor.com/images/45fe45f75ec523c2abf4e75ca2ac2fe2/tenor.gif?itemid=11797931")
        embed.set_footer(text="Command: 9cookie @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True) #Cookies Command
    async def cookies(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person has gave you a bunch of cookies", description="**{1}** gave cookies to **{0}**! :cookie:".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Cookies sent by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url="https://media1.tenor.com/images/30c8ce96272fe73f58841164a179f6d1/tenor.gif?itemid=17729544")
        embed.set_footer(text="Command: 9cookies @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True) #Bonk Command
    async def bonk(self, ctx, member: discord.Member):
        """Shoot someone."""
        embed = discord.Embed(title="**Bonk!**", description="**{1}** Bonked **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Bonked by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url="https://media1.tenor.com/images/0f145914d9e66a19829d7145daf9abcc/tenor.gif?itemid=19401897")
        embed.set_footer(text="Command: 9bonk @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True) #Hug Command
    async def hug(self, ctx, member: discord.Member):
        """Hug someone."""
        embed = discord.Embed(title="Sending...", description="**{1}** hugs **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Hugged by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url="https://media1.tenor.com/images/29a4aef07fde6e590aeaa3381324bbd1/tenor.gif?itemid=18630098")
        embed.set_footer(text="Command: 9hug @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True) #Kiss Command
    async def kiss(self, ctx, member: discord.Member):
        embed = discord.Embed(title="*This person gave you a suprise!*", description="**{1}** kissed **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Kissed by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url="https://media1.tenor.com/images/4700f51c48d41104e541459743db42ae/tenor.gif?itemid=17947049")
        embed.set_footer(text="Command: 9kiss @user | (Covid Free)")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True, aliases=['fb', 'bump']) #Fistbump Command
    async def fistbump(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person gave you a fistbump ;)", description="**{1}** fistbumped **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Fistbumped by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url="https://media2.giphy.com/media/l0HlL6XHioKD5Gsgg/giphy.gif?cid=ecf05e473oo7yozme81o170s0i9tjwxdb7pq69ba46acewt0&rid=giphy.gif")
        embed.set_footer(text="Command: 9fistbump @user | 9fb @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True, aliases=['frick', 'fuck']) #Frick Command
    async def sex(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person had sex with you ;)", description="**{1}** fucked **{0}**!".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Fricked by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url="https://media1.tenor.com/images/fa98b23ca1dba1925da62f834f27153f/tenor.gif?itemid=19355212")
        embed.set_footer(text="Command: 9frick @user | 9fuck @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True, aliases=['do', 'donu']) #Donut Command
    async def donut(self, ctx, member: discord.Member):
        embed = discord.Embed(title="This person gave you donut!", description="**{1}** gave donut to **{0}** :doughnut:".format(member.name, ctx.message.author.name), color=0x680af5)
        embed.set_author(name="Donut sent by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_image(url="https://media1.tenor.com/images/29a1be900e68a176097ff05eb51514b5/tenor.gif?itemid=8158743")
        embed.set_footer(text="Command: 9donut @user | 9do @user")
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(client):
    client.add_cog(fun(client))
