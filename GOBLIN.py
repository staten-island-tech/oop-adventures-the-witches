class Goblin: 
    import random

    def __init__(self, name, health, inventory, personality, weapon, tricks):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.personality = personality
        self.weapon = weapon
        self.tricks = tricks
    def trickery(self, treasure):
        print (f"{self.name}: ")
