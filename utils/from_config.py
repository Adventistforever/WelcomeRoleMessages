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
            return 'Error'


def load_dm_roles():

    if config.ROLES_FOR_DM is not None:
        try:
            return [int(role) for role in config.ROLES_FOR_DM]
        except (ValueError, TypeError):
            print(
                "Error in config.py - Please check that ROLES_FOR_DM value is valid."
            )
            return 'Error'

def load_channel_role():

    if config.ROLE_FOR_CHANNEL_MSG is not None:
        try:
            return int(config.ROLE_FOR_CHANNEL_MSG)
        except (ValueError, TypeError):
            print(
                "Error in config.py - Please check that ROLE_FOR_CHANNEL_MSG value is valid."
            )
            return 'Error'


def load_send_channel():

    if config.SEND_CHANNEL is not None:
        try:
            return int(config.SEND_CHANNEL)
        except (ValueError, TypeError):
            print(
                "Error in config.py - Please check that SEND_CHANNEL value is valid."
            )
            return 'Error'


def load_dm_msg(role_id):
    path = None
    for file in listdir("./data/dm"):
        if file.endswith(f"{role_id}.txt"):
            path = f'./data/dm/{file}'
            with open(path) as f:
                return f.read()

    return 'Error'


def load_channel_msg(role_id):
    path = None
    for file in listdir("./data/channel"):
        if file.endswith(f"{role_id}.txt"):
            path = f'./data/channel/{file}'
            with open(path) as f:
                return f.read()

    return 'Error'



def check_config():

    if load_error_send_target() != 'Error':
        if load_dm_roles() != 'Error':
            if load_channel_role() != 'Error':
                if load_send_channel()!= 'Error':
                    return True

    return False



def check_dm_messages():

    role_ids = load_dm_roles()

    if role_ids is not None:
        role_ids = [str(role) for role in role_ids]
        for file in listdir('./data/dm'):
            if not file.startswith('sample'):
                test = [role for role in role_ids if role in file]
                if not bool(test):
                    return False
    return True


def check_channel_messages():

    ch_role = load_channel_role()
    if ch_role is not None:
        files = listdir('./data/channel')
        if not bool([file for file in files if str(ch_role) in file]):
            return False

    return True

