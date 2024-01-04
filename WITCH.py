class Witch:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    def battle(self, MCinventory):
        print("After the rain had cleared, you were back on your journey...")
        print("Days later you have arrived at the Witch's Coven...\nYou head in, and there's the witch...waiting for you....\n")
        if MCinventory == []:
            print ("Uh oh...you have no weapons...")
            print (f"{self.name} won the battle!")
            print (f"{self.name}: Of course I would win...")
            return (f"YOU LOST THE FINAL BATTLE!")
        weapon = input(f"Which weapon would you like to equip from your inventory?\n{MCinventory}")
        if weapon == ("Wooden Broom") or ("Wooden Cane"):
            move = input("What move do you do? (Slash, Stab, ")
            
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
            print (f"{self.witchinventory} was dropped.")
            return ("YOU WON THE FINAL BATTLE! CONGRATULATIONS!")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print (f"{self.name}: Of course I would win...")
            return (f"YOU LOST THE FINAL BATTLE!")