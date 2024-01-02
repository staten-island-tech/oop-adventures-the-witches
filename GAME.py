from GNOME import Forestgnome
from MAINCHARACTER import Maincharacter
from BANDIT import Bandit
from ICEDRAGON import Icedragon

mcNAME = input("START OF WITCH COVEN ADVENTURE \nWhat is your name? ")
papagnome = Forestgnome("Papa Forest Gnome", 250, "What is seen in the middle of March and April that can't be seen at the beginning or end of either month? ", "r", 3, "Wooden Cane")
mc = Maincharacter(mcNAME, 1000, ["Wooden Cleaning Broom"], [])
bandit = Bandit("???", 375, "Knife", [], ["Healing Potion", "Shield Potion", "Tommy Gun","Croissant"])
icey = Icedragon("Icey", 1000, "Icicle Storm", ["Gold Sword", "Gold Bow"])

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
    banditBATTLE = bandit.battle(mc.name, mc.inventory, ["Sword of Light", "Shield Potion", "Crossaint", "Strength Potion", "Healing Potion"])
    print (banditBATTLE)
Part2Bandit()

def Part3IceDragon():
    start = icey.start()
    print (start)
    