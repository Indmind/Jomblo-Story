import json

def setUserInfo(key, value):
    data = {
            key: value
            }
    with open('data/info.json', 'w') as f:
        json.dump(data, f)

def getUserInfo():
    with open('data/info.json', 'r') as f:
        return json.load(f)

# print(getUserInfo()['name'])
