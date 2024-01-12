class Bandit:
    def __init__(self, name, health, weapon, inventorySTEAL):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.inventorySTEAL = inventorySTEAL
    
    def sneaky(self, MCname, MCitems, MCinventory):
        print (f"{MCname}: Whats that sound? I thought I heard something...")
        self.inventorySTEAL.append(MCitems)
        MCinventory = []
        print (f"Inventory: \n{MCinventory}")
        return (f"You're missing {MCitems}!!!")

    def battle(self, MCname, MCinventory, items, selected_number, MChealth):
        run = input ("Uh oh, do you want to run after the thief? ")
        if run == ("No"):
            return ("Okay..you might not see those items again...")
        elif run == ("Yes"):
            input("\nYou run after the thief through the crowded, busy streets.")
            input("Through the rush, you knock over someone's stand.")
            stand = input("Do you help? ")
            if stand == ("Yes"):
                input("You fix the stand, which takes more time than you thought...")
                input("However, the owner, grateful for your help, hands you a bag with an item.")
                MCinventory.append(items)
                input (f"Inventory: \n{MCinventory}\nWow...who was that person?")
                return("Unfortunately, it seems like the bandit got away...")
            elif stand == ("No"):
                woods = input("You leave the unfortunate owner scrambling to fix up the stand...\n\nYou continue running after the bandit, who goes into the woods.\nDo you continue? ")
                if woods == ("Yes"):
                    input(f"The bandit suddenly stops and you catch up.")
                    input(f"{MCname}: Give me my items back!!!")
                    weapons = input("Wait...looks like you don't have any weapons...Do you still wish to fight? ")
                    if weapons == ("Yes"):
                        count = 0
                        while self.health>0 and MChealth>0:
                            move = input("What move do you do? (Punch, Kick, Slap) ")
                            if move == ("Punch"):
                                print ("You punched the bandit.")
                                self.health = self.health-100
                                print (f"Bandit health: {self.health}")
                            elif move == ("Kick"):
                                print ("You kicked the bandit.")
                                self.health = self.health-200
                                print (f"Bandit health: {self.health}")
                            elif move == ("Slap"):
                                print ("You slapped the bandit.")
                                self.health = self.health-80
                                print (f"Bandit health: {self.health}")
                            else:
                                return ("That is not a move.")
                            number_now = selected_number[count]
                            if self.health<=0:
                                break
                            if number_now == ("one"):
                                print ("The bandit slashes a knife at you!")
                                MChealth=MChealth-150
                                print (f"{MCname}'s health: {MChealth}")
                            elif number_now == ("three")\
                            or number_now == ("two"):
                                print ("The bandit stabs you! ")
                                MChealth=MChealth-300
                                print (f"{MCname}'s health: {MChealth}")
                            count = count + 1
                        return ()
                    elif weapons == ("No"):
                        return("Okay..you might not see those items again...")
                elif woods == ("No"):
                    return("Okay..you might not see those items again...")
                else:
                    return ("You did not respond to the question.")
            else:
                return("You did not respond to the question.")
        else:
            return("You did not respond to the question.")

    def battleoutcome(self, MCitems):
        if self.health <= 0:
            input (f"{self.name} has been defeated. ")
            input (f"{self.weapon} has been dropped. ")
            input (f"You won {MCitems} back!!")
            return (f"{self.inventorySTEAL} was dropped!")
        elif self.health>0:
            input (f"{self.name} won the battle!")
            return (f"{self.name}: I guess I'm keeping all these items!")