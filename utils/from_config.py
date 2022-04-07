import config
from os import listdir, path




def load_error_send_target():
    if config.ERROR_SEND_TARGET is not None:
        try:
            return int(config.ERROR_SEND_TARGET)
        except (ValueError, TypeError):
            print(
                "Error in config.py - Please check that ERROR_SEND_TARGET value is valid."
            )
            return "Error"


def load_dm_roles():
    if config.ROLES_FOR_DM is not None:
        try:
            return [int(role) for role in config.ROLES_FOR_DM]
        except (ValueError, TypeError):
            print("Error in config.py - Please check that ROLES_FOR_DM value is valid.")
            return "Error"


def load_channel_roles():
    if config.ROLE_FOR_CHANNEL_MSG is not None:
        try:
            return [int(role) for role in config.ROLE_FOR_CHANNEL_MSG]
        except (ValueError, TypeError):
            print(
                "Error in config.py - Please check that ROLE_FOR_CHANNEL_MSG value is valid."
            )
            return "Error"


def load_send_channel():
    if config.SEND_CHANNEL is not None:
        try:
            return int(config.SEND_CHANNEL)
        except (ValueError, TypeError):
            print("Error in config.py - Please check that SEND_CHANNEL value is valid.")
            return "Error"


def load_dm_msg(role_id):
    path = None
    for file in listdir("./data/dm"):
        if file.endswith(f"{role_id}.txt"):
            path = f"./data/dm/{file}"
            with open(path) as f:
                return f.read()

    return "Error"


def load_channel_msg():
    with open("./data/channel/message.txt") as f:
        return f.read()


def load_auto_remove_role():
    if config.AUTO_REMOVE_ROLE is not None:
        try:
            return int(config.AUTO_REMOVE_ROLE)
        except (ValueError, TypeError):
            print('Error in config.py - Please check that AUTO_REMOVE_ROLE value is valid')
            return 'Error'

