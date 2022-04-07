# imported from native python modules
from datetime import time, datetime
from os import listdir, getenv, path
from json import dump

# imported from custom modules in utils
from utils import from_config, db

# third party import - disnake (discord python library)
from disnake import Intents
from disnake.ext import commands, tasks
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

    await bot.wait_until_ready()
    auto_remove_role.start()
    print(f"{bot.user} is alive and listening for Discord events.")



@tasks.loop(time=time(0,0))
async def auto_remove_role():
    '''
    iterate bot guilds, and find the role that matches configured role, then remove that role from
    the member if the current date is less than timestampe'''
    auto_remove_role_id = from_config.load_auto_remove_role()
    today_timestamp = datetime.timestamp(datetime.now())

    for guild in bot.guilds:
        auto_remove_role = guild.get_role(int(auto_remove_role_id))

        if not auto_remove_role is None:

            # load the member and timestamp for comparison
            data = db.load_members_json()
            members = data['members']

            for member in members:
                for k,v in member.items():
                    if v < today_timestamp:
                        get_member = guild.get_member(int(k))
                        if auto_remove_role in get_member.roles:
                            await get_member.remove_roles(auto_remove_role)




def member_json():
    '''check if member.json exists, if not create it'''
    if not path.exists('./data/members.json'):
        with open('./data/members.json','w') as f:
            dump({"members": []}, f, indent=4)



if __name__ == "__main__":
    # run pre_run_check, if pass run bot
    member_json()
    load_dotenv()
    bot.run(getenv("TOKEN"))
