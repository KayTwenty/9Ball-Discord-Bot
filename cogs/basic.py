import discord
import random

from discord.ext import commands
from utils.colors import *

class basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command() #The Main 9Ball command
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
                    "Ask an admin",
                    "Maybe Not.",
                    "Nie.",
                    "Negative.",
                    "Definitely yes!",
                    "I can see it as true.",
                    "I can see it as false.",
                    "Idk m8... Ask Murphy...",
                    "Oh hecc naw!",
                    "Definitely."]

        embed=discord.Embed(title="The official 9Ball has Spoken.", color=random.choice(colors))
        embed.set_author(name="Asked by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Question:", value=question, inline=False)
        embed.add_field(name="Answer:", value=random.choice(responses), inline=False)
        embed.set_footer(text="Commands: 9ball | 9help")
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(client):
    client.add_cog(basic(client))
