import json

cfg = {}

try:
    with open("config.json", "r") as file:
        cfg = json.load(file)
except Exception as err:
    print(err)

def get(key):
    if key in cfg:
        return cfg[key]

def edit(key, value):
    if key in cfg:
        cfg[key] = value
        save()

def save():
    with open("../config.cfg", 'w') as configfile:
        configfile.write(json.dump(cfg))