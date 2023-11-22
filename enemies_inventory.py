import json
test = open("data.json", encoding="utf8")
data = json.load(test)

def allenemiesEncounters():
    print ("ENEMY DATABASE -- SEARCH FOR ONE OF THE FOLLOWING ENEMIES:")
    for i in range (6):
        everything = (list(data[i].values())) #all values in data
        print (everything[0])
allenemiesEncounters()

def allenemiesSEARCH():
    #Organizes inputs: makes sure the input is one of the listed enemies before continuing.
    for i in range (6):
        everything = (list(data[i].values()))
    enemy = input("Search for an enemy: ")
    if enemy == everything[0]:
        pass
    else:
        print ("No such enemy.")
        return
    
    search = input("What do you wish to search for? (Enemy Description, Enemy Stats, Enemy Moves): ")
   
   #Searches description of enemies
    if search == ("desc"): 
        for i in range (6):
            everything = (list(data[i].values())) # all values in data
            if enemy == (everything[0]):
                print (f"{everything[0]}: {everything[5]}")
                print (f"Power: {everything[2]}")

    #Searches stats of enemies
    elif search == ("stats"):
        for i in range (6):
            everything = (list(data[i].values())) # all values in data
            if enemy == (everything[0]):
                print (f"{everything[0]}: Strength: {everything[3]}/10, Health: {everything[-1]}")
    
    #Searches moves of enemies
    elif search == ("moves"):
        for i in range (6):
            everything = (list(data[i].values())) # all values in data
            if enemy == (everything[0]):
                print (f"{everything[0]}: {everything[4]}")


    else:
        print ("No such search value.")

allenemiesSEARCH()