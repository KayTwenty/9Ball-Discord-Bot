import discord
import random
import asyncpraw

from discord.ext import commands
from utils.colors import *


class reddit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        reddit = asyncpraw.Reddit(
            client_id="fHs5tuKe-KWd_Q",
            client_secret="lxDKogyfylCqTlxWTUuhtkNkemo",
            user_agent="reddit.py",
        )

        subreddit = await reddit.subreddit("memes")
        all_subs = []
        top = subreddit.top(limit=35)
        async for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(
            title=name, description="Using Reddit API", color=random.choice(colors)
        )
        embed.set_author(
            name="Used by: " + str(ctx.message.author),
            icon_url=ctx.message.author.avatar_url,
        )
        embed.set_image(url=url)
        embed.add_field(name="View Online", value=f"[Link]({url})")
        embed.set_footer(text="Commands: 9meme")
        await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(reddit(client))
