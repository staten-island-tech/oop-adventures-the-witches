class Witch:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    def battle(self, MCinventory, MChealth):
        print("After the rain had cleared, you were back on your journey...")
        print("Days later you have arrived at the Witch's Coven...\nYou head in, and there's the witch...waiting for you....\n")
        if MCinventory == []:
            print ("Uh oh...you have no weapons...")
            print (f"{self.name} won the battle!")
            print (f"{self.name}: Of course I would win...")
            return (f"YOU LOST THE FINAL BATTLE!")
        weapon = input(f"Which weapon would you like to equip from your inventory?\n{MCinventory}")
        if weapon == ("Wooden Cleaning Broom") or ("Wooden Cane") or "Knife":
            input("What move do you do? (Slash, Stab) ")
            return (f"{self.name} broke your weapon in half!!")
        elif weapon == ("")
        else:
            return ("That's not a proper response.")
    def result(self):
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
            return ("YOU WON THE FINAL BATTLE! CONGRATULATIONS!")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print (f"{self.name}: Of course I would win...")
            return (f"YOU LOST THE FINAL BATTLE!")
        