class Witch:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    def start():
        print("After the rain had cleared, you were back on your journey...")
        return("Days later you have arrived at the Witch's Coven...\nYou head in, and there's the witch...waiting for you....\n")
    def battle(self, MCinventory, MChealth, number):    
        if MCinventory == []:
            print ("Uh oh...you have no weapons...")
            print (f"{self.name} won the battle!")
            print (f"{self.name}: Of course I would win...")
            return (f"YOU LOST THE FINAL BATTLE!")
        weapon = input(f"Which weapon would you like to equip from your inventory?\n{MCinventory}")
        if weapon == ("Wooden Cleaning Broom") or ("Wooden Cane") or ("Knife"):
            input("What move do you do? (Slash, Stab) ")
            print (f"{self.name} broke your weapon in half!!\n{self.name} won the battle!\n{self.name}: Of course I would win...")
            return (f"YOU LOST THE FINAL BATTLE!")
        elif weapon == ("Tommy Gun"):
            return(f"Before you could even do anything, the witch used her staff and crushed your weapon!!\n{self.name} won the battle!\n{self.name}: Of course I would win...")
        elif weapon == ("Sword of Light") or ("Gold Sword"):
            while self.health>0 and MChealth>0:
                move = input("What move do you do? (Slash, Stab, Throw) ")
                if move == ("Slash"):
                    print ("You run forward and slash the witch.")
                    newhealth = self.health-500
                    newhealth = self.health
                    print (f"Witch: {self.health-500}")
                    if number == ("one"):
                        print ("The witch casts a dark spell on you...")
                        print (f"You: {MChealth-100}")
                    elif number == ("two"):
                        print ("The witch uses her staff to expel you backwards...")
        elif weapon == ("Gold Bow"):
            print ()
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
        