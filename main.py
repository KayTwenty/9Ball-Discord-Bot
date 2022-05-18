import discord
import os

from discord.ext import commands
from discord.ext.commands import MissingPermissions
from utils.constants import BOT_TOKEN, BOT_PREFIX


client = commands.Bot(
    command_prefix=BOT_PREFIX,
    intents=discord.Intents.all(),
    allowed_mentions=discord.AllowedMentions(
        everyone=False, users=True, roles=False, replied_user=True
    ),
    case_insensitive=True
)
client.remove_command("help")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# CMD Screen when Bot starts
@client.event
async def on_ready():
    print("Logged in as: " + client.user.name + "\n")
    print("Servers connected to:")
    for guild in client.guilds:
        print(guild.name)


# Error ignore for MissingPermissions
@client.event
async def on_command_error(error):
    if isinstance(error, MissingPermissions):
        return


# Errormessage
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.reply(f">>> **I just found an error!**\n{error}")


try:
    client.run(BOT_TOKEN)
except Exception as e:
    print(f"Error when logging in: {e}")
