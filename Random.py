import steamfront
import requests
import random
import time
from steam.steamid import SteamID
from decouple import config
from steam.webapi import WebAPI
from steam.client.user import SteamUser
from steam.client.builtins.user import User
from steam.client import SteamClient
from steam.enums.emsg import EMsg
from Loading import animation

API = str(input("API key :"))
id64Steam = str(input("id64 :"))

# Get the list from the API
SteamList = 'http://api.steampowered.com/ISteamApps/GetAppList/v0001/' 
dictGames = requests.get(SteamList)

# Get the list from the dictionary
jsonGames = dictGames.json()
AllgameList = jsonGames["applist"]["apps"]["app"]


#client = SteamClient()           we can possibly add features with this 
clientGame = steamfront.Client(API)

user = clientGame.getUser(id64=id64Steam)
apps = user.raw_apps  # Steam games of the user
userList = [None] * len(apps)

#client.cli_login() 

#print("Logged on as: %s" % client.user.name)

for i in range(len(apps)):
    userList[i] = apps[i]["appid"]
# Now we got the list with all the appid from all the games of the user (in userList)

for id in range(len(userList)):
    for k in range(len(AllgameList)):
        if AllgameList[k]["appid"] == userList[id] :     # <----- we convert appid into names from the database
            userList[id] = AllgameList[k]["name"]
# Now we got the list of names from the game library of the user

animation() # Animation with the moving bars

print("Game :",random.choice(userList),"!")

#client.logout()