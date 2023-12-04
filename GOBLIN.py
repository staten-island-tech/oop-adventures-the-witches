class Goblin: 

    def __init__(self, name, health, inventory, personality, weapon, tricks):
        self.name = name
        self.health = health
        self.inventoryTREASURE = inventory
        self.personality = personality
        self.weapon = weapon
        self.tricks = tricks
    def battleoutcome(self):
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
            print (f"Oh, whats this? {self.inventoryTREASURE} has been dropped. ")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print ("Hehehe, I knew I would win !")