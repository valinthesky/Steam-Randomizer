import random
import requests
import json
import sys, string, os
from typing import Final
from SteamRequest import SteamID
import steam.webauth as wa
import steamapi
from steamUser import steamUser

SID = input("Enter your SteamID: ")
AUTH = input("Enter your AUTH key: ")

user = steamUser(SID, AUTH)
print(user.getUser())
print(user.getBans())

def __init__(self,id):
    self.id = id


steamapi.core.APIConnection(api_key=AUTH, validate_key=True)












# print("The game selected is: ", FinalGame)
#if FinalGame == "Terraria":
#   os.system('cmd /c start steam://rungameid/105600')
#if FinalGame == "Rocket League":
#    os.system('cmd /c start steam://rungameid/252950')
#if FinalGame == "Trackmania" :
#    os.system('cmd /c start steam://rungameid/11020')
#print("... Launching your game")
