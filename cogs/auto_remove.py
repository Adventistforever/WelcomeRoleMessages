from datetime import datetime, timedelta
from disnake.ext import commands
from utils import from_config, db



class RemoveRole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Cog Loaded: {self.qualified_name}')


    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        '''
        runs when a member is updated

        This function is to monitor if a member is assigned a role.
        Store this member and the time stamp (7 days) to remove the "Freshly joined role"

        Parameters
        ----------
        before, after: Member objects the represent the member before and after
        the update.
        '''
        guild = before.guild
        auto_remove_role = guild.get_role(from_config.load_auto_remove_role())
        check_roles = [guild.get_role(r_id) for r_id in from_config.load_dm_roles()]

        # load json data members list
        data = db.load_members_json()

        # if remove role in before roles and any monitored role in after roles,
        # store the member with datetime now +  7 days
        if auto_remove_role in before.roles and any(role in check_roles for role in after.roles):

            future_timestamp = datetime.timestamp(datetime.now() + timedelta(days=+7))
            member_id = str(after.id)

            if not [[m_id for m_id in item.keys() if m_id == member_id] for item in data['members']]:
                data['members'].append({member_id: future_timestamp})

                # update the member.json list
                db.update_member_json(data)



def setup(bot):
    bot.add_cog(RemoveRole(bot))