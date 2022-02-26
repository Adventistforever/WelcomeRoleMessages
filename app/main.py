# imported from native python modules
from os import listdir

# imported from custom modules in utils
from utils import config

# third party import - disnake (discord python library)
from disnake import Intents
from disnake.ext import commands


# Instantiate bot and declare intents
intents = Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)


# load cog extenstions
for filename in listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


# simple on ready event -runs only once when bot connects to discord
@bot.listen()
async def on_ready():
    print(f"{bot.user} is alive and listening for Discord events.")


# run the bot using the secret token
bot.run(config.fetch_token())
