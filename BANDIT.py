class Bandit:
    def __init__(self, name, health, personality, weapon, inventorySTEAL):
        self.name = name
        self.health = health
        self.personality = personality
        self.weapon = weapon
        self.inventorySTEAL = inventorySTEAL
    def sneaky(self, MCitems, MCinventory):
        print ("Whats that sound? I thought I heard something...")
        self.inventorySTEAL.append(MCitems)
        print (MCinventory.remove(MCitems))
        print (f"You're missing {MCitems}!!!")
        run = input ("Uh oh, should you run after them?")
        if run == ("No"):
            print ("Okay..you might not see those items again...")
        elif run == ("Yes"):
            print ("Be prepared for battle!")
            