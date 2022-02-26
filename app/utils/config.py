from json import load as jload, dump as jdump
from os import listdir


# load config.json into dict
def fetch_config():
    with open('./config.json') as f:
        return jload(f)


# fetch the bot token from config.json - return the bot token string
def fetch_token():
    config = fetch_config()
    return config['bot_token']


# fetch roles from json - return list of role IDs
def fetch_role_ids():
    config = fetch_config()
    role_ids = []
    for role in config['roles']:

        try:
            role_id = int(role)
            role_ids.append(role_id)

        except ValueError:
            break
            return 'ValueError'

    return role_ids

def fetch_error_msg_target():
    config = fetch_config()
    try:
        target = int(config['error_send_target'])
        return target
    except ValueError:
        return 'ValueError'


def fetch_dm_msg(role_id: str):
    for filename in listdir('./data'):
        if filename.endswith(f'{role_id}.txt'):
            with open(f'./data/{filename}') as f:
                return f.read()
        else:
            return 'Error'
