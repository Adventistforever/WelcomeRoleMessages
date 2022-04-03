# imported from native python modules
from os import listdir, getenv

# imported from custom modules in utils
from utils import from_config

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


if __name__ == "__main__":
    # check the configs, then run the bot
    if from_config.check_config():

        if from_config.check_dm_messages():

            if from_config.check_channel_messages():

                print()
                print("Config is valid and message files are present!")
                print("---------------------------------------------")
                bot.run(getenv("bot_token"))

            else:
                print(
                    "Channel Message File Error: You are missing the .txt file in /data/channels/ for the monitored role in config.py"
                )
        else:
            print(
                "DM Message File Error: You are missing one or more .txt files in /data/dm/ for the monitored roles in config.py"
            )
