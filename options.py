import json

def get_options():
    with open('/data/options.json') as file:
        options = json.load(file)
        return options
