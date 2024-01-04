class Icedragon:
    def __init__(self, name, health, weapon, treasure):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.treasure = treasure
    def start(self, MCfriendinventory):
        cave = input("\n\nAfter the long day, you decide to move on from Crystal Cliffs and follow the path to leave.\nIt's a few days after you had left Crystal Cliffs. \nYou are very, very tired and all of a sudden, it starts pouring. \nTheres a cozy cave on the side of the road.\n You decide it's best to head in.\nAfter being out of the rain, you realize the cave leaves further down into a passageway. \nDo you explore or stay on the outer area of the cave? ")
        if cave == ("Explore"):
            run = input ("You decide to explore and go through the narrow tunnel...\nThe cave seems to be much larger than you had previously thought, and you soon walk into a large, open area of the cave where a large dragon rests..\nIt hears you, and screeches loudly.\nDo you run or fight? ")
            if run == ("Fight"):
                print ("You decide to stay and fight...")
            ###import battle later
                if self.health <= 0:
                    print (f"{self.name} has lost. ")
                    print (f"{self.weapon} has been dropped. ")
                    friendship = input (f"Befriend {self.name}? ")
                    if friendship == ("No"):
                        print (f"{self.name} has been defeated.")
                    elif friendship == ("Yes"):
                        print (f"You just gained an ally! \nYou can call {self.name} to battle anytime.")
                        MCfriendinventory.append({self.name})
                    else:
                        return("That is not a proper response.")
                elif self.health > 0:
                    print (f"{self.name} won the battle!")
                    return (f"{self.name}:...")
            elif run == ("Run"):
                return ("You decide to run back out into the narrow tunnels and stay on the outside of the cave, waiting for the rain to stop.")
            else:
                return("That is not a proper response.")
        elif cave == ("Stay"):
            return ("You decide to stay on the outside of the cave...\nAfter a while, you find yourself drifting off into sleep...")
        else:
            return ("That is not a proper response.")