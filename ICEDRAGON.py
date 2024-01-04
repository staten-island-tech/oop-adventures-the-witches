class Icedragon:
    def __init__(self, name, health, weapon, treasure):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.treasure = treasure
    def start(self):
        cave = input("\n\nAfter the long day, you decide to move on from Crystal Cliffs and follow the path to leave.\nIt's a few days after you had left Crystal Cliffs. \nYou are very, very tired and all of a sudden, it starts pouring. \nTheres a cozy cave on the side of the road.\n You decide it's best to head in.\nAfter being out of the rain, you realize the cave leaves further down into a passageway. \nDo you explore or stay on the outer area of the cave?")
        if cave == "Stay":
            return("Today seems to be a peaceful day. Nothing happens.")
        if cave == "Explore":
            print("A giant ice dragon has awakened from its slumber. It taunts you.")
        else:
            return("That is not a proper response.")
        battle = input("Will you accept the fight? Y/N")
        if battle == ("Yes"):
            return()##battle
        elif battle == ("No"):
            return("You run out of the gloomy cave.")
            
    
    def battleoutcome(self, MCfriendinventory):
        if self.health <= 0:
            print (f"{self.name} has lost. ")
            print (f"{self.weapon} has been dropped. ")
            friendship = input (f"Befriend {self.name}?")
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