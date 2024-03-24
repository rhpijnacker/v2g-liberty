import json

def get_config():
    with open('/data/config.json') as file:
        data = json.load(file)
        return data
