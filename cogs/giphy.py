import discord
import asyncio
import random
import giphy_client
from giphy_client.rest import ApiException 
from discord.ext import commands
from random import choice

class giphy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx,*,q="random"):

        api_key="sXMtRpE8GuySsLQNj1OIKk0Acqzaqrls"
        api_instance = giphy_client.DefaultApi()

        try: 
        # Search Endpoint
        
            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)
            colors = [0x680af5,0x2E10ED,0x8CF9C1,0xF88000,0xFCFF00,0xed129f,0xed3212,0x1ACFE7,0x0FD150,0xFE2D00]

            emb = discord.Embed(title=q, description="Using Giphy API", color=random.choice(colors))
            emb.set_author(name="Command used by: " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
            emb.set_footer(text="Commands: 9gif | 9gif dog")

            await ctx.reply(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


def setup(client):
    client.add_cog(giphy(client))