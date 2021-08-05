'  Importing from config.py  '
from discord.errors import ClientException
from data.config import *
import gtts
from gtts import gTTS
from discord.utils import get

class tts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel=None):

        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise InvalidVoiceChannel('No channel to join. Please either specify a valid channel or join one.')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Moving to channel: <{channel}> timed out.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Connecting to channel: <{channel}> timed out.')

        await ctx.send(f'Connected to: **{channel}**', delete_after=20)

    @commands.command()
    async def repeat(self, ctx, *, text=None):

        if not text:
            # We have nothing to speak
            await ctx.send(f"Hey {ctx.author.mention}, I need to know what to say please.")
            return

        vc = ctx.voice_client # We use it more then once, so make it an easy variable
        if not vc:
            # We are not currently in a voice channel
            await ctx.send(f"Hey {ctx.author.mention}, use `9join` to connect to channel. I know, I can't get it automatically to join the call. It's still work in progress...")
            return

        # Lets prepare our text, and then save the audio file
        tts = gTTS(text=text, lang="en", tld="co.uk")
        tts.save("text.mp3")

        try:
            # Lets play that mp3 file in the voice channel
            vc.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f"Finished playing: {e}"))

            # Lets set the volume to 1
            vc.source = discord.PCMVolumeTransformer(vc.source)
            vc.source.volume = 1

        # Handle the exceptions that can occur
        except ClientException as e:
            await ctx.send(f"A client exception occured:\n`{e}`")
        except TypeError as e:
            await ctx.send(f"TypeError exception:\n`{e}`")
    
    @commands.command()
    async def disconnect(self, ctx):
        """
        Disconnect from a voice channel, if in one
        """
        vc = ctx.voice_client

        if not vc:
            await ctx.send("I am not in a voice channel.")
            return

        await vc.disconnect()
        await ctx.send("I have left the voice channel!")

def setup(bot):
    bot.add_cog(tts(bot))