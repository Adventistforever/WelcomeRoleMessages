from json import load, dump


def load_members_json():
    with open('./data/members.json') as f:
        return load(f)

def update_member_json(data):
    with open('./data/members.json', 'w') as f:
        dump(data, f, indent=4)