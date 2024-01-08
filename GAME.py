from GNOME import Forestgnome
from MAINCHARACTER import Maincharacter
from BANDIT import Bandit
from ICEDRAGON import Icedragon
from WITCH import Witch
import random
number = ["one", "two", "three"]
selected_number = random.choice(number)

mcNAME = input("START OF WITCH COVEN ADVENTURE \nWhat is your name? ")
papagnome = Forestgnome("Papa Forest Gnome", 250, "What is seen in the middle of March and April that can't be seen at the beginning or end of either month? ", "r", 3, "Wooden Cane")
mc = Maincharacter(mcNAME, 1000, ["Wooden Cleaning Broom"], [])
bandit = Bandit("???", 375, "Knife", [], ["Tommy Gun"])
icey = Icedragon("Icey", 1000, "Icicle Storm", ["Gold Sword", "Gold Bow"])
witch = Witch("???", 10000, "Magic Staff")
def StartGnome():
    start = papagnome.start()
    print(start)
    if papagnome.health == 0:
        gnomeBATTLEresult = papagnome.battleresult()
        print (gnomeBATTLEresult)
        mcVICTORY = mc.victory(papagnome.weapon)
        print (mcVICTORY)
StartGnome()

def Part2Bandit():
    print("As always, the small town of Crystal Cliffs is bustling and busy.\nYou wander around the middle of town, which is crowded with small shops and villagers.")
    banditSTEAL = bandit.sneaky(mc.name, mc.inventory, mc.inventory)
    print (banditSTEAL)
    mc.inventory = []
    banditBATTLE = bandit.battle(mc.name, mc.inventory, ["Sword of Light"])
    print (banditBATTLE)
Part2Bandit()

def Part3IceDragon():
    start = icey.start(mc.friends)
    print (start)
Part3IceDragon()

def ENDWitch():
    start = witch.start()
    print (start)
    battle = witch.battle(mc.inventory, mc.health, selected_number)
    print (battle)
    
ENDWitch()