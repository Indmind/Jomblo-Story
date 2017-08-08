import json

def getUserInfo():
    with open('data/info.json', 'r') as f:
        return json.load(f)

def setUserInfo(data):
    oldData = getUserInfo()
    oldData.update(data)
    with open('data/info.json', 'w') as f:
        json.dump(oldData, f)

def getCharInfo():
    with open('data/char.json', 'r') as f:
        data = json.load(f)
        return data

def setCharInfo(data):
    oldData = getCharInfo()
    oldData.update(data)
    with open('data/char.json', 'w') as f:
        json.dump(oldData, f)
