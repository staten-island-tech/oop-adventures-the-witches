class Witch:
    def __init__(self, name, health, personality, weapon, power, witchinventory):
        self.name = name
        self.health = health
        self.personality = personality
        self.weapon = weapon
        self.power = power
        self.witchinventory = witchinventory


    def battleoutcome(self):
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
            print (f"{self.witchinventory} was dropped.")
            print ("YOU WON THE FINAL BATTLE! CONGRATULATIONS!")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print (f"{self.name}: Of course I would win...")
            print (f"YOU LOST THE FINAL BATTLE!")