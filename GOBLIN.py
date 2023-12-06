class Goblin: 
    def __init__(self, name, health, inventory, personality, weapon, tricks):
        self.name = name
        self.health = health
        self.inventoryTREASURE = inventory
        self.personality = personality
        self.weapon = weapon
        self.tricks = tricks
    def treasure(self, MCshinyitem, MCinventory):
        print (f"{self.name}: What is that...")
        self.inventoryTREASURE.append(MCshinyitem)
        MCinventory.remove(MCshinyitem)
    def battleoutcome(self, MCshinyitem):
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
            print (f"Oh, whats this? {self.inventoryTREASURE} has been dropped. Turns out {self.name} had stolen {MCshinyitem}!")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print (f"{self.name}: Hehehe, I knew I would win! Guess you're not getting {MCshinyitem} back!")