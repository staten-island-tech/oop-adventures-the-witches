from GNOME import Forestgnome
from MAINCHARACTER import Maincharacter
from BANDIT import Bandit

mcNAME = input("START OF WITCH COVEN ADVENTURE \nWhat is your name? ")
papagnome = Forestgnome("Papa Forest Gnome", 250, "What is seen in the middle of March and April that can't be seen at the beginning or end of either month? ", "r", 3, "Wooden Cane")
mc = Maincharacter(mcNAME, 1000, ["Wooden Cleaning Broom"])
bandit = Bandit("???", 375, "Knife", [], ["Healing Potion", "Shield Potion", "Tommy Gun","Croissant"])

def Start_Gnome():
    roadsChoice = input("It was a dark stormy evening. \nAs a young maiden you have just finished work. \nTired and annoyed of the rich family you work for, you slowly head down the wet path leading up to the hill. \nYou see a sign that reads 'Left: Wickery Hills', 'Right: Crystal Cliffs'. \nWhich way do you go? ")
    if roadsChoice == ("Left"):
        wickery_hills = input("You head up the path towards Wickery Hills. However you don't seem to remember this path. Go back? ")
        if wickery_hills == ("Yes"):
            investigate = input("Wait...This isn't the way I came from.... \n*Sound of leaves rustling.* \nWould you like to investigate the noise? ")
            if investigate == ("Yes"):
                print("You begin to approach the bushes...")
                riddle = papagnome.ask()
                print(riddle)
                if papagnome.health == 0:
                    gnomeBATTLEresult = papagnome.battleresult()
                    print (gnomeBATTLEresult)
                    mcVICTORY = mc.victory(papagnome.weapon)
                    print (mcVICTORY)
                elif papagnome.health > 0:
                    run = input(f"{papagnome.name}: Hahahaha...I knew a lowly human like yourself would not be able to answer!\nDo you wish to run away or fight? ")
                    if run == ("Run"):
                        print("You run away towards Crystal Cliffs.")
                    elif run == ("Fight"):
                        #import moves and battle
                        print("jaskdf")
            elif investigate == ("No"):
                print ("You ignore the noise and continue walking.\nWait a second...\nIs that the entrance to Crystal Cliffs?\nYou really don't know your way around...")
        elif wickery_hills == ("No"):
            print("You continue walking.\nHuh...you really don't remember this place...\nWait is that the entrance to Crystal Cliffs?")
    if roadsChoice == ("Right"):
        print ("You head up the path towards Crystal Cliffs.")
Start_Gnome()

def Part2Bandit():
    print("As always, the small town of Crystal Cliffs is bustling and busy.\nYou wander around the middle of town, which is crowded with small shops and villagers.")
    banditSTEAL = bandit.sneaky(mc.name, mc.inventory)
    print (banditSTEAL)
    if banditSTEAL == ("Yes"):
        
Part2Bandit()