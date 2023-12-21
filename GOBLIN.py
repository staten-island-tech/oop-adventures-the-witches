class Goblin: 
    def __init__(self, name, health, inventory, weapon):
        self.name = name
        self.health = health
        self.inventoryTREASURE = inventory
        self.weapon = weapon
    def treasure(self, MCshinyitem, MCinventory):
        print (f"{self.name}: What is that...")
        self.inventoryTREASURE.append(MCshinyitem)
        MCinventory.remove(MCshinyitem)
    def beginning(self):
        stay = input ("After a long and tiring day, you try to decide where you'd like to stay for the night.\nCliffs' Inn, which is quite a walk away as it is on the other side of town, or the village bench right next to you? ")
        if stay == ("village bench"):
            print ("\n\nYou decide Cliffs' Inn is too far and so you plop down on the bench and quickly fall asleep after your busy day.")
        elif stay == ("Cliffs' Inn"):
            print ("\n\nWith the cold weather, you decide sleeping outside is too unsafe and decide the 1 and a half hour walk will be worth it.\nAfter a dreadful walk in the cold, you are so tired and quickly fall asleep on the cozy bed after your very long journey.")
            
    def battleoutcome(self, MCshinyitem):
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
            return (f"Oh, whats this? {self.inventoryTREASURE} has been dropped. Turns out {self.name} had stolen {MCshinyitem}!")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            return (f"{self.name}: Hehehe, I knew I would win! Guess you're not getting {MCshinyitem} back!")