class Witch:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
<<<<<<< HEAD
        self.power = power
        self.witchinventory = witchinventory


    def battleoutcome(self):
=======
    def Start(self):
        print("After the rain had cleared, you were back on your journey...")
        print("Days later you have arrived at the Witch's Coven...\nYou head in, and there's the witch...waiting for you....\n")
        ###import battle
>>>>>>> 7c8e13db1a33787cbf450023c49b692f263fd225
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
            print (f"{self.witchinventory} was dropped.")
            return ("YOU WON THE FINAL BATTLE! CONGRATULATIONS!")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print (f"{self.name}: Of course I would win...")
            return (f"YOU LOST THE FINAL BATTLE!")