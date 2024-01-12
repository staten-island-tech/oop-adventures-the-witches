class Forestgnome:
    def __init__(self, name, health, riddle, riddleanswer, chances, weapon):
        self.name = name
        self.health = health
        self.riddle = riddle
        self.riddleanswer = riddleanswer
        self.chances = chances
        self.weapon = weapon
    def start(self, MCinventory, MCname, MChealth, selected_number):
        input("It was a dark stormy evening.")
        input("As a young maiden you have just finished work.")
        input("Tired and annoyed of the rich family you work for, you slowly head down the wet path leading up to the hill.")
        input("You see a sign that reads 'Left: Wickery Hills', 'Right: Crystal Cliffs Village'.")
        roadsChoice = input("Which way do you go? ")
        if roadsChoice == ("Left"):
            input("You head up the path towards Wickery Hills.")
            input("However, you don't seem to remember this path.")
            wickery_hills = input("Go back? ")
            if wickery_hills == ("Yes"):
                input("Wait...This isn't the way I came from....")
                input("*Sound of leaves rustling.*")
                investigate = input("Would you like to investigate the noise? ")
                if investigate == ("Yes"):
                    input("You begin to approach the bushes...")
                    riddle = input(f"{self.name}: {self.riddle}")
                    if riddle == self.riddleanswer:
                        self.health = 0
                        return (f"{self.name}: NOOOO!!! No one has ever answered correctly before!!")
                    elif riddle != self.riddleanswer:
                        input ("Be prepared for battle!!!")
                        input(f"{self.name}: Hahahaha...I knew a lowly human like yourself would not be able to answer!")
                        run = input("Do you wish to run away or fight? ")
                        if run == ("Run"):
                            return("You run away towards Crystal Cliffs Village.")
                        elif run == ("Fight"):
                            weapon = input(f"Which weapon would you like to equip from your inventory?\n{MCinventory} ")
                            if weapon == ("Wooden Cleaning Broom"):
                                count = 0
                                while self.health>0 and MChealth>0:
                                    move = input("What move do you do? (Slash, Stab) ")
                                    if move == ("Slash"):
                                        print ("You slash the gnome.")
                                        self.health = self.health-50
                                        print (f"Gnome health: {self.health}")
                                    elif move == ("Stab"):
                                        print ("You stab the gnome.")
                                        self.health = self.health-100
                                        print (f"Gnome health: {self.health}")
                                    else:
                                        return ("That is not a move.")
                                    number_now = selected_number[count]
                                    if self.health<=0:
                                        break
                                    if number_now == ("one"):
                                        print ("The gnome swings its wooden cane at you!")
                                        MChealth=MChealth-80
                                        print (f"{MCname}'s health: {MChealth}")
                                    elif number_now == ("three")\
                                    or number_now == ("two"):
                                        print ("The gnome stabs you with its cane!")
                                        MChealth=MChealth-150
                                        print (f"{MCname}'s health: {MChealth}")
                                    count = count + 1
                                return ()
                        else:
                            return("That is not a proper response.")
                    else:
                        return("That is not a proper response.")
                elif investigate == ("No"):
                    input ("You ignore the noise and continue walking.")
                    input("Wait a second...")
                    input("Is that the entrance to Crystal Cliffs Village?")
                    return ("You really don't know your way around...")
                else:
                    return("That is not a proper response.")
            elif wickery_hills == ("No"):
                input("You continue walking.")
                input("Huh...you really don't remember this place...")
                return("Wait is that the entrance to Crystal Cliffs Village?")
            else:
                return ("That is not a proper response.")
        elif roadsChoice == ("Right"):
            return ("You head up the path towards Crystal Cliffs Village.")
        else:
            return ("That is not a proper response.")
    
    def battleresult(self):
        if self.health <= 0:
            input (f"{self.name} has been defeated.")
            return (f"{self.weapon} was dropped.")
        elif self.health > 0:
            input (f"{self.name} won the battle!")
            return (f"{self.name}: Haha, I knew I would win!!")