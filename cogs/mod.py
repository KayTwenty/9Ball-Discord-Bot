# mod.py
# This is a cog

import discord

from discord.ext import commands


class mod(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['delete', 'purge', 'c', 'remove']) #Best clear command I've ever done
    async def clear(self, ctx, amount: int):
        if ctx.message.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(title=f"`{amount}` messages were removed.", description="", color=0xff0000)
            await ctx.send(embed=embed, delete_after=3)
        else:
            embed = discord.Embed(title="Error:", description="Role must need manage messages to be enabled.", color=0xff0000)
            await ctx.send(embed=embed, delete_after=8)
    
    @commands.command(aliases=['bl'], pass_context=True)     
    async def blacklist(self, ctx, user_id: int):
        author = ctx.message.author
        guild = author.guild

        user = guild.get_member(user_id)
        if user is not None:
            return await ctx.invoke(self.ban, user=user)

        try:
            await self.client.http.ban(user_id, guild.id, 0)
            await ctx.send(content=self.client.command_prefix + 'Banned user: %s' % user_id)
        except discord.NotFound:
            await ctx.send(content=self.client.command_prefix + 'Could not find user. '
                               'Invalid user ID was provided.')
        except discord.errors.Forbidden:
            await ctx.send(content=self.client.command_prefix + 'Could not ban user. Not enough permissions.')
       

def setup(client):
    client.add_cog(mod(client))