# imported from native python modules
from os import listdir, getenv

# imported from custom modules in utils
from utils import from_config

# third party import - disnake (discord python library)
from disnake import Intents
from disnake.ext import commands
from dotenv import load_dotenv


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


def pre_run_check():
    return all(
        (
            from_config.check_config(),
            from_config.check_dm_messages(),
            from_config.check_channel_messages(),
        )
    )


if __name__ == "__main__":
    # run pre_run_check, if pass run bot
    if pre_run_check():
        print()
        print("All configs and messages are valid and present")
        print("----------------------------------------------")
        load_dotenv()
        bot.run(getenv("TOKEN"))
    else:
        print(
            "Error: Please check config.py for invalid values and ensure all role messages are present"
        )
