# imported from custom modules in utils
from utils import from_config

# third party import - disnake (discord python library)
from disnake import Embed, errors
from disnake.ext import commands


class RoleMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ready message when cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Cog Loaded: {self.qualified_name}")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """
        On member update listener
        Listening for role update events

        Parameters
        ----------
        - before: member object, before the role change
        - after : member object, after the role change
        """
        guild = before.guild
        member = before

        # fetch the dm_roles and ch_role from config
        dm_roles = [guild.get_role(int(role)) for role in from_config.load_dm_roles()]
        ch_roles = [
            guild.get_role(int(role)) for role in from_config.load_channel_roles()
        ]

        if any(dm_roles) is None:
            print(
                "DM Roles Error: There was an error fetching a role from the guild. Check config.py for invalid entries."
            )
            return

        if any(ch_roles) is None:
            print(
                "Channel Roles Error: There was an error fetching a role from the guild. Check config.py for invalid entries."
            )
            return

        # if the new role is a channel role, send the message to the target channel
        roles = [
            role
            for role in ch_roles
            if role not in before.roles and role in after.roles
        ]
        if bool(roles):

            ch_role_channel_id = from_config.load_send_channel()
            ch_role_msg = from_config.load_channel_msg()

            ch_role_channel = guild.get_channel(int(ch_role_channel_id))
            if ch_role_channel is None:
                print(
                    f"Channel ID Error: {ch_role_channel_id} is not a valid channel in your guild."
                )

            msg = ch_role_msg.replace("{member}", member.mention).replace(
                "{role}", roles[0].mention
            )
            await ch_role_channel.send(msg)

        else:
            for dm_role in dm_roles:
                if dm_role not in before.roles and dm_role in after.roles:

                    dm_message = from_config.load_dm_msg(dm_role.id)
                    err_msg_target = from_config.load_error_send_target()

                    embed = Embed(
                        title=f"[{dm_role.name}] was added to your roles!",
                        description=dm_message,
                    )
                    if guild.icon:
                        embed.set_thumbnail(url=guild.icon.url)

                    try:
                        await member.send(embed=embed)
                    except errors.Forbidden:
                        # couldn't send DM to member due to permissions

                        # check if target is a member or channel
                        channel = guild.get_channel(int(error_target))
                        error_member = guild.get_member(int(error_target))

                        if channel:
                            await channel.send(err_msg)
                        elif error_member:
                            await error_member.send(err_msg)
                        else:
                            print(
                                'Error in config.py - The supplied "error_send_target" value is not valid.'
                            )
                            return


def setup(bot):
    bot.add_cog(RoleMessage(bot))
