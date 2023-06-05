import steamfront, requests, random, time, os
from Loading import animation

API = str(input("API key :"))
id64Steam = str(input("id64 :"))
os.system('cls||clear')

# Get the list from the API
SteamList = 'http://api.steampowered.com/ISteamApps/GetAppList/v0001/' 
dictGames = requests.get(SteamList)

# Get the list from the dictionary
jsonGames = dictGames.json()
AllgameList = jsonGames["applist"]["apps"]["app"]


clientGame = steamfront.Client(API)

user = clientGame.getUser(id64=id64Steam)
apps = user.raw_apps  # Steam games of the user
userList = [None] * len(apps)

ChooseGame = None

while ChooseGame == None : # Some games in the library may not be in the actual steam database
    for i in range(len(apps)):
        userList[i] = apps[i]["appid"]
    # Now we got the list with all the appid from all the games of the user (in userList)

    ChooseGameID = random.choice(userList)

    for id in range(len(userList)):
        for k in range(len(AllgameList)):
            if AllgameList[k]["appid"] == ChooseGameID :     # <----- we convert appid into a name from the database
                ChooseGame = AllgameList[k]["name"]

animation() # Animation with the moving bars

print("Game :",ChooseGame,"!")

while True:
    response = str(input("Do you wanna launch the game ? (y/n): "))
    if response == "y":
        os.system('cmd /c start steam://rungameid/{}'.format(ChooseGameID))
        time.sleep(3)
        break
    elif response == "n":
        print("Goodbye !")
        break
    else : 
        os.system('cls||clear')
        print("Please enter (y/n)...")


