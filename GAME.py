from GNOME import Forestgnome
from MAINCHARACTER import Maincharacter
def Start_Gnome():
    mcNAME = input("START OF WITCH COVEN ADVENTURE \nWhat is your name? ")
    roadsChoice = input("It was a dark stormy evening. \nAs a young maiden you have just finished work. \nTired and annoyed of the rich family you work for, you slowly head down the wet path leading up to the hill. \nYou see a sign that reads 'Left: Wickery Hills', 'Right: Crystal Cliffs'. \nWhich way do you go? ")
    if roadsChoice == ("Left"):
        papagnome = Forestgnome("Papa Forest Gnome", 250, "What is seen in the middle of March and April that can't be seen at the beginning or end of either month? ", "r", 3, "Heavy Wooden Stick")
        mc = Maincharacter(mcNAME, 1000, ["Wooden Broom"])
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
                # elif papagnome.health > 0:

            elif investigate == ("No"):
                print ("You ignore the noise and continue walking.")
        elif wickery_hills == ("No"):
            print("You continue walking.\nHuh...you really don't remember this place...\nWait, is that the sign for Crystal Cliffs?")
    # if roadsChoice == ("Right"):

Start_Gnome()

