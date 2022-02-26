# imported from custom modules in utils
from utils import config

# third party import - disnake (discord python library)
from disnake import Embed, errors
from disnake.ext import commands



class RoleMessage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # ready message when cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Cog Loaded: {self.qualified_name}')


    '''
    On member update listener
    Listening for role update events

    --Parameters --
    - before: member object, before the role change
    - after : member object, after the role change
    '''
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = before.guild
        member = before
        # fetch the monitored role IDs from json
        role_ids = config.fetch_role_ids()

        '''
        Check that role_ids is a list of interger IDs, if not, print the ValueError error to console
        '''
        if role_ids != 'ValueError':
            for role_id in role_ids:
                role = guild.get_role(role_id)

                # if a role has been added, run checks and send DM
                if not role in before.roles and role in after.roles:
                    message = config.fetch_dm_msg(role.id)

                    # if message has not been setup for the monitored role, send error message to console
                    if message == 'Error':
                        print(f'The custom message for {role.name} has not been setup - please add the {role.name}-{role.id}.txt file to /data')

                    else:
                        embed = Embed(
                            title=f'[{role.name}] was added to your roles!', description=message
                            )
                        if guild.icon:
                            embed.set_thumbnail(url=guild.icon.url)

                        # try to send the embed to the member DM, if fails, send to channel/member target
                        try:
                            await member.send(embed=embed)

                        except errors.Forbidden:
                            # can't send DM, get error_msg_target ID from config.json
                            target = config.fetch_error_msg_target()

                            if target is None:
                                pass

                            elif target == 'ValueError':
                                print(f'Error: The provided value is not does match any channels or members in {guild.name}')

                            else:
                                message = f'{member.mention} was assigned a new role, **{role.name}**, but I could not DM them the custom message.'

                                '''
                                Check if the returned target ID from json is a channel.
                                if it's not a not a channel, check if member
                                if neither, print error to console
                                if member, send the error message to the target member
                                if channel, send the error message to the target channel
                                '''
                                channel = guild.get_channel(target)
                                if channel is None:
                                    target_member = guild.get_member(target)
                                    if target_member is None:
                                        print(f'An error occurred. No member or channel with ID [{target}] found.')
                                    else:
                                        await target_member.send(message)
                                else:
                                    await channel.send(message)

        else:
            print(f'Error: One more role ID values are incorrect. Please check config.json and verify the "roles" values.')







def setup(bot):
    bot.add_cog(RoleMessage(bot))