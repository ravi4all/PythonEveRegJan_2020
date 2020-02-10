import json
import urllib.request as url

name = input("Enter name of cricketer : ")
path = f"https://cricapi.com/api/playerFinder?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&name={name}"
res = url.urlopen(path)
data = json.load(res)
player_id = data['data'][0]['pid']

path_2 = f"https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid={player_id}"
res = url.urlopen(path_2)
data = json.load(res)

info = data['data']
bat = info['batting']
batting_data = bat['ODIs']
for item in batting_data:
    print(item,"==>",batting_data[item])
