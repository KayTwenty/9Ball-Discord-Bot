'  Importing from config.py  '
from data.config import *


if os.path.exists(os.getcwd() + "/data/config.json"):
    with open("./data/config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "9"}
    with open(os.getcwd() + "/data/config.json", "w+") as f:
        json.dump(configTemplate, f)

TOKEN = configData["Token"]
BOT_PREFIX = configData["Prefix"]

client = commands.Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

async def status(): #Status changer for the bot
    while True:
        await client.wait_until_ready()
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Happy July!!"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Version 2.6"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9help | 9b"))
        await sleep(3600)
        await client.change_presence(activity=discord.Streaming(name="Smort Nerd", url="https://www.twitch.tv/sodapoppin"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9gif"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9clear"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("VSCode"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Ask me Question"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9meme"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("World of Time"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("NineBall, your local questioneer!"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("9b"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Raw Spaghetti Laser Beam!"))
        await sleep(3600)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Summer Time"))
        await sleep(3600)

'  The start screen  '
@client.event #CMD Screen when Bot starts
async def on_ready():
    users = len(set(client.get_all_members()))
    ping = (time.monotonic()) / 10000
    print('-----------------------------------------------------------------------------')
    print(str(datetime.datetime.now().time()) + " - Connecting to Discord API...")
    print(str(datetime.datetime.now().time()) + " - Connected to Discord API.")
    print(str(datetime.datetime.now().time()) + " - Loading stats and posting to DBL...")
    print(str(datetime.datetime.now().time()) + " - Loading complete!")
    print("Logged in as: " + client.user.name + "\n")
    print("{} users".format(users))
    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)
    print('------------------------------------------------------------------------------')
client.loop.create_task(status())

'  The Reload command  '
@commands.check(ownercheck)
@client.command(aliases=["refresh"])
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send("9Ball has reloaded the cog!")

' The Errorhandling  '
@client.event #Error ignore for MissingPermissions
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        return

'  The Errorhandling  '
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.reply(f">>> **I just found an error!**\n{error}")  # Errormessage


client.run(TOKEN)
