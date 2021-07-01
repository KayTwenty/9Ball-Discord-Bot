'  Importing from config.py  '
from config import *

class giphy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx,*,q="random"):

        api_key="sXMtRpE8GuySsLQNj1OIKk0Acqzaqrls"
        api_instance = giphy_client.DefaultApi()

        try: 
        # Search Endpoint
        
            api_response = api_instance.gifs_search_get(api_key, q, limit=40, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=q, description="Using Giphy API", color=random.choice(colors))
            emb.set_author(name="Command used by: " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
            emb.set_footer(text="Commands: 9gif | 9gif dog")

            await ctx.reply(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

def setup(client):
    client.add_cog(giphy(client))