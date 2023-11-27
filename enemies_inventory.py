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
    #User input for enemy
    enemy = input ("Which enemy do you wish to know more about? ")


   #Searches description of enemies
    search = input("What do you wish to search for? (Enemy Description, Enemy Stats, Enemy Moves): ")
    if search == ("desc"): 
        for i in range (6):
            everything = (list(data[i].values())) # all values in data
            if enemy == (everything[0]):
                print (f"{everything[0]}: {everything[5]}")
                print (f"Power: {everything[2]}")
        if enemy != (everything[0]):
            print ("No such enemy.")
            
    #Searches stats of enemies
    elif search == ("stats"):
        for i in range (6):
            everything = (list(data[i].values())) # all values in data
            if enemy == (everything[0]):
                print (f"{everything[0]}: Strength: {everything[3]}/10, Health: {everything[-1]}")  
        if enemy != (everything[0]):
            print ("No such enemy.")    
    
    #Searches moves of enemies
    elif search == ("moves"):
        for i in range (6):
            everything = (list(data[i].values())) # all values in data
            if enemy == (everything[0]):
                print (f"{everything[0]}: {everything[4]}")
        if enemy != (everything[0]):
            print ("No such enemy.")
    else:
        print ("No such enemy and/or search value.")

allenemiesSEARCH()