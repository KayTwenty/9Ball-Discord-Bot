'  Importing from config.py  '
from data.config import *

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

        embed=discord.Embed(title="The official 9Ball has Spoken.", color=random.choice(colors))
        embed.set_author(name="Asked by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Question:", value=question, inline=False)
        embed.add_field(name="Answer:", value=random.choice(responses), inline=False)
        embed.set_footer(text="Commands: 9ball | 9help")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(aliases=['Help', 'h']) #The 9Ball help commands...
    async def help(self, ctx):
        embed=discord.Embed(title="9Ball Main Help Commands", color=0x680af5)
        embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="9ball *Your Question*", value="9Ball answers your desired question.", inline=False)
        embed.add_field(name="9clear 5", value="9Ball deletes server messages by a selected number.", inline=False)
        embed.add_field(name="9stats", value="9Ball lists the stats.", inline=False)
        embed.add_field(name="9gif", value="9Ball will pull gifs from Giphy", inline=False)
        embed.add_field(name="9about", value="The about page for 9Ball.", inline=False)
        embed.add_field(name="9blacklist *UserID*", value="Blacklists any user which is not in server using user's ID", inline=False)
        embed.set_footer(text="Commands: 9help2 for page 2")
        await ctx.reply(embed=embed)
    
    @commands.command(aliases=['funhelp', 'fun']) #Fun 9ball commands
    async def help2(self, ctx):
        embed=discord.Embed(title="9Ball Fun Help Commands", color=0x680af5)
        embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="9cookie @user", value="Gives cookie to the selected user.", inline=False)
        embed.add_field(name="9bonk @user", value="9Ball bonks the selected user.", inline=False)
        embed.add_field(name="9hug @user", value="Gives a hug to the selected user.", inline=False)
        embed.add_field(name="9kiss @user", value="Kisses user (Covid free).", inline=False)
        embed.add_field(name="9fistbump @user", value="fistbump user.", inline=False)
        embed.add_field(name="9frick @user", value="Oh yeah bb!!.", inline=False)
        embed.add_field(name="9donut @user", value="Gives donut to user.", inline=False)
        embed.add_field(name="9ship @user @user", value="9Ball will ship two selected users.", inline=False)
        embed.add_field(name="9gay @user", value="9Ball will determine the gay percent on the selected user.", inline=False)
        embed.set_footer(text="Commands: 9help for page 1")
        await ctx.reply(embed=embed)
    
def setup(client):
    client.add_cog(basic(client))
