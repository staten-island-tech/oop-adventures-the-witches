from GNOME import Forestgnome
from MAINCHARACTER import Maincharacter
from BANDIT import Bandit
from ICEDRAGON import Icedragon
from WITCH import Witch
import random
number_list = ["one", "two", "three"]
selected_number = random.choices(number_list, k = 100)

mcNAME = input("START OF WITCH COVEN ADVENTURE \nWhat is your name? ")
input ("Directions: When answering questions, please type your answer with the first letter capitalized. Have fun!")
papagnome = Forestgnome("Papa Forest Gnome", 250, "What is seen in the middle of March and April that can't be seen at the beginning or end of either month? ", "r", 3, "Wooden Cane")
mc = Maincharacter(mcNAME, 1000, ["Wooden Cleaning Broom"])
bandit = Bandit("???", 375, "Knife", ["Tommy Gun"])
icey = Icedragon("Icey", 4000, "Icicle Storm", ["Gold Sword", "Gold Bow"])
witch = Witch("???", 10000, "Magic Staff")
def StartGnome():
    start = papagnome.start(mc.inventory, mc.name, mc.health, selected_number)
    print(start)
    if papagnome.health <= 0:
        gnomeBATTLEresult = papagnome.battleresult()
        print (gnomeBATTLEresult)
        mcVICTORY = mc.victory(papagnome.weapon, 1000)
        print (mcVICTORY)
StartGnome()

def Part2Bandit():
    input("As always, the small town of Crystal Cliffs is bustling and busy.")
    input("You wander around the middle of town, which is crowded with small shops and villagers.")
    banditSTEAL = bandit.sneaky(mc.name, mc.inventory, mc.inventory)
    print (banditSTEAL)
    banditBATTLE = bandit.battle(mc.name, mc.inventory, ["Sword of Light"], selected_number, mc.health)
    print (banditBATTLE)
    if bandit.health<=0:
        banditBATTLEresult = bandit.battleoutcome(mc.inventory)
        print (banditBATTLEresult)
        mcVICTORY = mc.victory ([bandit.weapon, bandit.inventorySTEAL], 3000)
        print (mcVICTORY)
Part2Bandit()

def Part3IceDragon():
    start = icey.start(mc.inventory, mc.health, mc.name, selected_number)
    print (start)
    if icey.health<=0:
        iceyBATTLEresult = icey.battleoutcome()
        print (iceyBATTLEresult)
        mcVICTORY = mc.victory (icey.treasure, 5000)
        print (mcVICTORY)
Part3IceDragon()

def ENDWitch():
    start = witch.start()
    print (start)
    battle = witch.battle(mc.inventory, mc.health, selected_number, mc.name)
    print (battle)
    result = witch.result()
    print (result)
ENDWitch()