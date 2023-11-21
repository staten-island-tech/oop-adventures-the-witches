import json
test = open("data.json", encoding="utf8")
data = json.load(test)

def allenemiesEncounters():
    for i in range (6):
        everything = (list(data[i].values())) # all values in data
        print (everything[0])
allenemiesEncounters()

def allenemiesSEARCH():
    search = input("What do you wish to search for? (Enemy Description, Enemy Stats, Enemy Moves): ")
    if search == ("desc"): 
        enemy = input("Search for an enemy: ")
        for i in range (6):
            everything = (list(data[i].values())) # all values in data
            if enemy == (everything[0]):
                print (f"{everything[0]}: {everything[5]}")
                print (f"Power: {everything[2]}")
    elif search == ("stats"):
        enemy = input ("Search for an enemy: ")
        for i in range (6):
            everything = (list(data[i].values())) # all values in data
            if enemy == (everything[0]):
                print (f"{everything[0]}: Strength: {everything[3]}/10, Health: {everything[-1]}")
    elif search == ("moves"):
        enemy = input ("Search for an enemy: ")
        for i in range (6):
            everything = (list(data[i].values())) # all values in data
            if enemy == (everything[0]):
                print (f"{everything[0]}: {everything[4]}")
allenemiesSEARCH()