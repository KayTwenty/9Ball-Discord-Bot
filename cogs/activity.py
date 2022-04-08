from discord.ext import commands
from discord_together import DiscordTogether
from utils.constants import BOT_TOKEN

class activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether(BOT_TOKEN)
        
    @commands.command()
    async def poker(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
        await ctx.send(f"Click the blue link!\n{link}")
    
    @commands.command()
    async def chess(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
        await ctx.send(f"Click the blue link!\n{link}")
        
    @commands.command()
    async def betrayal(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
        await ctx.send(f"Click the blue link!\n{link}")
    
    @commands.command()
    async def fishing(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
        await ctx.send(f"Click the blue link!\n{link}")


def setup(bot):
    bot.add_cog(activity(bot))