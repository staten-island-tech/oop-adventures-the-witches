class Witch:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    def start(self):
        input("After the rain had cleared, you were back on your journey...")
        input("Days later you have arrived at the Witch's Coven...")
        input("You head in, and there's the witch...waiting for you....")
    def battle(self, MCinventory, MChealth, selected_number, MCname):    
        if MCinventory == []:
            input ("Uh oh...you have no weapons...")
            input (f"{self.name} won the battle!")
            input (f"{self.name}: Of course I would win...")
            return (f"YOU LOST THE FINAL BATTLE!")
        weapon = input(f"Which weapon would you like to equip from your inventory?\n{MCinventory} ")
        if weapon == ("Wooden Cleaning Broom")\
        or weapon == ("Wooden Cane")\
        or weapon == ("Knife"):
            input("What move do you do? (Slash, Stab) ")
            print (f"{self.name} broke your weapon in half!!")
            MChealth = 0
        elif weapon == ("Tommy Gun"):
            print(f"Before you could even do anything, the witch used her staff and crushed your weapon!!")
            MChealth = 0
        elif weapon == ("Sword of Light")\
        or weapon == ("Gold Sword")\
        or weapon == ("Gold Bow"):
            count = 0
            while self.health>0 and MChealth>0:
                move = input("What move do you do? (Slash, Stab, Throw) ")
                if move == ("Slash"):
                    print ("You run forward and slash the witch.")
                    self.health = self.health-500
                    print (f"Witch health: {self.health}")
                elif move == ("Stab"):
                    print ("You stab the witch.")
                    self.health = self.health-500
                    print (f"Witch health: {self.health}")
                elif move == ("Throw"):
                    print ("You throw your weapon at the witch.")
                    self.health = self.health-2000
                    print (f"Witch health: {self.health}")
                else:
                    return ("That is not a move.")
                number_now = selected_number[count]
                if self.health<=0:
                    break
                if number_now == ("one"):
                    print ("The witch casts a dark spell on you...")
                    MChealth=MChealth-800
                    print (f"{MCname}'s health: {MChealth}")
                elif number_now == ("two"):
                    print ("The witch uses her staff to expel you backwards...")
                    MChealth=MChealth-500
                    print (f"{MCname}'s health: {MChealth}")
                elif number_now == ("three"):
                    print ("The witch uses her staff to hit you.")
                    MChealth=MChealth-300
                    print (f"{MCname}'s health: {MChealth}")
                count = count + 1
            return ()
        else:
            return ("That's not a proper response.")
    def result(self):
        if self.health <= 0:
            input (f"{self.name} has been defeated. ")
            input (f"{self.weapon} has been dropped. ")
            return ("YOU WON THE FINAL BATTLE! CONGRATULATIONS!")
        elif self.health > 0:
            input (f"{self.name} won the battle!")
            input (f"{self.name}: Of course I would win...")
            return (f"YOU LOST THE FINAL BATTLE!")
        