import random
import requests
import subprocess
import sys, string, os
from typing import Final
from SteamRequest import steamUser

NomberGame = int(input("Choose the number of game : ",))
GameList = []
a = ""
n = 0

user = steamUser("Cervolen", "46AB1339F3B19BEB3426001A27E72B35")

userInfo = user.getUser()

gameCount, userGames = user.getGames()

vacBanned, banCount = user.getBans()
#Penser a rajouter les jeux qui peuvent être lancer

for i in range(0, NomberGame):
    a = input("Write the name of a game: ")
    GameList.insert(n, a)
    n = n+1 


FinalGame = random.choice(GameList)

print("The game selected is: ", FinalGame)

if FinalGame == "Terraria":
    os.system('cmd /c start steam://rungameid/105600')

if FinalGame == "Rocket League":
    os.system('cmd /c start steam://rungameid/252950')

if FinalGame == "Trackmania" :
    os.system('cmd /c start steam://rungameid/11020')


print("... Launching your game")
