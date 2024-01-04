import json
w = open("./weapon.json", encoding="utf8")
weapons = json.load(w)
m = open("./moves.json", encoding = "utf8")
moves = json.load(m)

class Forestgnome:
    def __init__(self, name, health, riddle, riddleanswer, chances, weapon):
        self.name = name
        self.health = health
        self.riddle = riddle
        self.riddleanswer = riddleanswer
        self.chances = chances
        self.weapon = weapon
    def start(self):
        roadsChoice = input("It was a dark stormy evening. \nAs a young maiden you have just finished work. \nTired and annoyed of the rich family you work for, you slowly head down the wet path leading up to the hill. \nYou see a sign that reads 'Left: Wickery Hills', 'Right: Crystal Cliffs Village'. \nWhich way do you go? ")
        if roadsChoice == ("Left"):
            wickery_hills = input("You head up the path towards Wickery Hills. However you don't seem to remember this path. Go back? ")
            if wickery_hills == ("Yes"):
                investigate = input("Wait...This isn't the way I came from.... \n*Sound of leaves rustling.* \nWould you like to investigate the noise? ")
                if investigate == ("Yes"):
                    print("You begin to approach the bushes...")
                    riddle = input(f"{self.name}: {self.riddle}")
                    if riddle == self.riddleanswer:
                        self.health = 0
                        return (f"{self.name}: NOOOO!!! No one has ever answered correctly before!!")
                    elif riddle != self.riddleanswer:
                        print ("Be prepared for battle!!!")
                        run = input(f"{self.name}: Hahahaha...I knew a lowly human like yourself would not be able to answer!\nDo you wish to run away or fight? ")
                        if run == ("Run"):
                            return("You run away towards Crystal Cliffs Village.")
                        elif run == ("Fight"):
                            return(f"{self.name} wants to fight!")
                        fight = input("Which weapon (and) items will you choose? Weapon:")
                        match_found = False
                        for weapon in MC.inventory:
                             if weapon["item"]["name"].lower() == fight.lower():
                        match_found = True 
                        print(f"Weapon found: {weapon['name']}")
                        if not match_found:
                            return("That is not in your inventory.")
                            ##actual fighting soon
                        print(f"{self.name} will attack first. Select a move: 1{self.move} or 2{self.move}.")
                        return({self.health} - {self.damage}.append)
                    print(f"{self.name} now has {self.health}")
                    return("That is not a proper response.")
                else:
                        return("That is not a proper response.")
            elif investigate == ("No"):
                    return ("You ignore the noise and continue walking.\nWait a second...\nIs that the entrance to Crystal Cliffs Village?\nYou really don't know your way around...")
                else:
                    return("That is not a proper response.")
        elif wickery_hills == ("No"):
                return("You continue walking.\nHuh...you really don't remember this place...\nWait is that the entrance to Crystal Cliffs Village?")
        else:
                return ("That is not a proper response.")
    elif roadsChoice == ("Right"): ##the indentition will make me do something bad.
return ("You head up the path towards Crystal Cliffs Village.")
        else:
            return ("That is not a proper response.")
    
    def battleresult(self):
        if self.health <= 0:
            print (f"{self.name} has been defeated.")
            return (f"{self.weapon} was dropped.")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            return (f"{self.name}: Haha, I knew I would win!!")