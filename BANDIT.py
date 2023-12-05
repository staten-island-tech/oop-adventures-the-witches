class Bandit:
    def __init__(self, name, health, personality, weapon, inventory, inventorySTEAL):
        self.name = name
        self.health = health
        self.personality = personality
        self.weapon = weapon
        self.inventorySTEAL = inventorySTEAL
        self.inventory = inventory
    def sneaky(self, MCitems, MCinventorybefore, MCinventoryafter): #MCinventoryafter does not have MCitems
        print ("Whats that sound? I thought I heard something...")
        self.inventorySTEAL.append(MCitems)
        print (f"Inventory: \n{MCinventorybefore.replace(MCinventorybefore, MCinventoryafter)}")
        print (f"You're missing {MCitems}!!!")
        run = input ("Uh oh, do you want to run after them?")
        if run == ("No"):
            print ("Okay..you might not see those items again...")
        elif run == ("Yes"):
            print ("Be prepared for battle!")
    def battleoutcome(self, MCitems, MCinventory):
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
            print (f"You won {MCitems} back!!")
            MCinventory.append(MCitems)
            self.inventorySTEAL.replace(self.inventorySTEAL, self.inventory)
            print (f"Oh, whats this? {self.inventorySTEAL} has been dropped. ")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print (f"{self.name}: I guess I'm keeping all these items!")
    
