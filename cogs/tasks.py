import discord

from discord.ext import commands, tasks
from asyncio import sleep


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status_handler.start()

    @tasks.loop()
    async def status_handler(self):
        await self.bot.wait_until_ready()
        await self.bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name="9help")
        )
        await sleep(500)
        await self.bot.change_presence(activity=discord.Game("Version: 3.0 Beta"))
        await sleep(500)
        await self.bot.change_presence(
            activity=discord.Game(f"with {len(self.bot.users)} humans!")
        )
        await sleep(500)
        await self.bot.change_presence(
            activity=discord.Game(f"in {len(self.bot.guilds)} servers")
        )
        await sleep(500)
        await self.bot.change_presence(
            activity=discord.Game("Raw Spaghetti Laser Beam!")
        )
        await sleep(500)


def setup(bot):
    bot.add_cog(Tasks(bot))
