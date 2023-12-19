class Bandit:
    def __init__(self, name, health, weapon, inventory, inventorySTEAL):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.inventorySTEAL = inventorySTEAL
        self.inventory = inventory
    def sneaky(self, MCname, MCitems, MCinventory):
        print (f"{MCname}: Whats that sound? I thought I heard something...")
        self.inventorySTEAL.append(MCitems)
        MCinventory = []
        print (f"Inventory: \n{MCinventory}")
        return (f"You're missing {MCitems}!!!")

    def battle(self, MCname, MCinventory, items, ):
        run = input ("Uh oh, do you want to run after the thief? ")
        if run == ("No"):
            return ("Okay..you might not see those items again...")
        elif run == ("Yes"):
            stand = input("\nYou run after the thief through the crowded, busy streets. Through the rush, you knock over someone's stand. \nDo you help? ")
            if stand == ("Yes"):
                print("You fix the stand, which takes more time than you thought...\nHowever, the owner, grateful for your help, hands you a bag full of items.")
                MCinventory.append(items)
                print (f"Inventory: \n{MCinventory}\nWow...who was that person?")
                return("Unfortunately, it seems like the bandit got away...")
            elif stand == ("No"):
                woods = input("You leave the unfortunate owner scrambling to fix up the stand...\n\nYou continue running after the bandit, who goes into the woods.\nDo you continue? ")
                if woods == ("Yes"):
                    return(f"The bandit suddenly stops and you catch up.\n{MCname}: Give me my items back!!!")
                ##import battle
                elif woods == ("No"):
                    return("Okay..you might not see those items again...")

    def battleoutcome(self, MCitems, MCinventory):
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
            print (f"You won {MCitems} back!!")
            MCinventory.append(MCitems)
            self.inventorySTEAL = self.inventory
            return (f"Oh, whats this? {self.inventorySTEAL} has been dropped. ")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            return (f"{self.name}: I guess I'm keeping all these items!")