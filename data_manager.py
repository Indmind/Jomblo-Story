import json

def setUserInfo(data):
    with open('data/info.json', 'w') as f:
        json.dump(data, f)

def getUserInfo():
    with open('data/info.json', 'r') as f:
        return json.load(f)

def getCharInfo():
    with open('data/char.json', 'r') as f:
        data = json.load(f)
        return data

def setCharInfo(data):
    #with open('data/char.json', 'w') as f:
    oldData = getCharInfo()
    oldData.update(data)
    with open('data/char.json', 'w') as f:
        json.dump(oldData, f)
# print(getUserInfo()['name'])
