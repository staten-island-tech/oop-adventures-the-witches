class Icedragon:
    def __init__(self, name, health, weapon, treasure):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.treasure = treasure
    def start(self, MCinventory, MChealth, MCname, selected_number):
        input("\n\nAfter the long day, you decide to move on from Crystal Cliffs and follow the path to leave.")
        input("\n\nIt's been a few days after you had left Crystal Cliffs.")
        input("You are very, very tired and all of a sudden, it starts pouring.") 
        input("Theres a cozy cave on the side of the road.") 
        input("You decide it's best to head in.")
        input("After being out of the rain, you realize the cave leaves further down into a passageway.")
        cave = input("Do you explore or stay on the outer area of the cave? ")
        if cave == ("Explore"):
            input ("You decide to explore and go through the narrow tunnel...")
            input("The cave seems to be much larger than you had previously thought, and you soon walk into a large, open area of the cave where a large dragon rests..")
            input("It hears you, and screeches loudly.")
            run = input("Do you run or fight? ")
            if run == ("Fight"):
                weapon = input(f"Which weapon would you like to equip from your inventory?\n{MCinventory} ")
                if weapon == ("Tommy Gun"):
                    print("Before you could even do anything, the icedragon used his claws and crushed your weapon!!")
                    MChealth = 0
                elif weapon == ("Wooden Cleaning Broom")\
                or weapon == ("Wooden Cane"):
                    input("What move do you do? (Slash, Stab) ")
                    print (f"{self.name} broke your weapon in half!!")
                    MChealth = 0
                elif weapon == ("Knife")\
                or weapon == ("Sword of Light"):
                    count = 0
                    while self.health>0 and MChealth>0:
                        move = input("What move do you do? (Slash, Stab, Throw) ")
                        if move == ("Slash"):
                            print ("You run forward and slash the dragon.")
                            self.health = self.health-300
                            print (f"Dragon health: {self.health}")
                        elif move == ("Stab"):
                            print ("You stab the dragon.")
                            self.health = self.health-800
                            print (f"Dragon health: {self.health}")
                        elif move == ("Throw"):
                            print ("You throw your weapon at the dragon.")
                            self.health = self.health-1000
                            print (f"Dragon health: {self.health}")
                        else:
                            return ("That is not a move.")
                        number_now = selected_number[count]
                        if self.health<=0:
                            break
                        if number_now == ("one"):
                            print ("The dragon uses magic to freeze you!")
                            MChealth=MChealth-1000
                            print (f"{MCname}'s health: {MChealth}")
                        elif number_now == ("two"):
                            print ("The dragon slams the ground around you, nearly breaking your bones!")
                            MChealth=MChealth-300
                            print (f"{MCname}'s health: {MChealth}")
                        elif number_now == ("three"):
                            print ("The dragon uses its claws and smacks you! ")
                            MChealth=MChealth-500
                            print (f"{MCname}'s health: {MChealth}")
                        count = count + 1
                    return ()
            elif run == ("Run"):
                return ("You decide to run back out into the narrow tunnels and stay on the outside of the cave, waiting for the rain to stop.")
            else:
                return("That is not a proper response.")
        elif cave == ("Stay"):
            return ("You decide to stay on the outside of the cave...\nAfter a while, you find yourself drifting off into sleep...")
        else:
            return ("That is not a proper response.")
    def battleoutcome(self):
        if self.health <= 0:
            input (f"{self.name} has been defeated. ")
            return (f"Oooh, whats this? {self.treasure} was dropped!!!")
        elif self.health > 0:
            input (f"{self.name} won the battle!")
            return (f"{self.name}:...")