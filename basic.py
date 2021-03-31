import discord
import random
from discord.ext import commands
from random import choice

class basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Ball', 'b', 'B']) #The Main 9Ball command
    async def ball(self, ctx, *, question):
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

        colors = [0x680af5,0x2E10ED,0x8CF9C1,0xF88000,0xFCFF00,0xed129f,0xed3212,0x1ACFE7,0x0FD150,0xFE2D00]
        embed=discord.Embed(title="The official 9Ball has Spoken.", color=random.choice(colors))
        embed.set_author(name="Asked by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Question:", value=question, inline=False)
        embed.add_field(name="Answer:", value=random.choice(responses), inline=False)
        embed.set_footer(text="Commands: 9ball | 9help")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(aliases=['Help', 'h']) #The 9Ball help commands...
    async def help(self, ctx):
        embed=discord.Embed(title="9Ball Help Commands", color=0x680af5)
        embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="9ball *Your Question*", value="9Ball answers your desired question.", inline=False)
        embed.add_field(name="9clear 5", value="9Ball deletes server messages by a selected number.", inline=False)
        embed.add_field(name="9cookie @user", value="Gives cookie to the selected user.", inline=False)
        embed.add_field(name="9bonk @user", value="9Ball bonks the selected user.", inline=False)
        embed.add_field(name="9hug @user", value="Gives a hug to the selected user.", inline=False)
        embed.add_field(name="9kiss @user", value="Kisses user (Covid free).", inline=False)
        embed.add_field(name="9fistbump @user", value="fistbump user.", inline=False)
        embed.add_field(name="9sex @user", value="Oh yeah bb!!.", inline=False)
        embed.add_field(name="9finger @user", value="Oh yes!!.", inline=False)
        embed.add_field(name="9stats", value="9Ball lists the stats.", inline=False)
        embed.add_field(name="9about", value="The about page for 9Ball.", inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(basic(client))