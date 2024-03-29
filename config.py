"""
Configure your bot using the variables below:  If you do not wish to use a specific
"""

#  can be a member ID, channel ID
ERROR_SEND_TARGET = 960109774370910238


# should be a comma separated list of role IDs you
# wish to monitor for custom DM messages
ROLES_FOR_DM = []

# should be a comma separated list of role IDs you
# wish to monitor for sending channel messages
ROLE_FOR_CHANNEL_MSG = [960123505511383130]

# the ID for the channel you wish the ROLE_FOR_CHANNEL_MSG to be sent to.
SEND_CHANNEL = 960103626674675772

# the ID for the role you wish to auto remove when one of the
# roles in ROLE_FOR_DM is assigned to the member
AUTO_REMOVE_ROLE = None

# the IDs for the roles you want to check for to start time for AUTO_REMOVE_ROLE
AUTO_REMOVE_ROLE_MONITOR = []


"""
message config functions - DO NOT ALTER
"""

from os import listdir, path


def load_dm_msg(role_id):
    path = None
    for file in listdir("./data/dm"):
        if role_id in file and file.endswith(".txt"):
            path = f"./data/dm/{file}"
            with open(path) as f:
                return f.read()


def load_channel_msg():
    with open("./data/channel/message.txt") as f:
        return f.read()


def get_error_target(guild):
    if ERROR_SEND_TARGET:
        member = guild.get_member(int(ERROR_SEND_TARGET))
        if member is None:
            channel = guild.get_channel(int(ERROR_SEND_TARGET))
            return channel

        return member
