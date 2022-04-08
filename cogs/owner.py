from discord.ext import commands
from utils.owners import *


class owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.check(ownercheck)
    @commands.command(aliases=["refresh"])
    async def reload(self, ctx, extension):
        self.client.unload_extension(f"cogs.{extension}")
        self.client.load_extension(f"cogs.{extension}")
        await ctx.send("9Ball has reloaded the cog!")


def setup(client):
    client.add_cog(owner(client))
