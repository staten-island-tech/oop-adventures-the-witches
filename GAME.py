def Roads_ForestGnome():
    roadsChoice = input("It was a dark stormy evening. \nAs a young maiden you had just finished work. \nTired and annoyed of the rich family you work for, you slowly head down the wet path leading up to the hill. \nYou see a sign that reads 'Left: Wickery Hills', 'Right: Crystal Cliffs'. \nWhich way do you go? ")
    if roadsChoice == ("Left"):
        from GNOME import Forestgnome
        papagnome = Forestgnome("Papa Forest Gnome", 250, "What is seen in the middle of March and April that can't be seen at the beginning or end of either month? ", "r", 3, "Wooden Cane")
        wickery_hills = input("You head up the path towards Wickery Hills. However you dont seem to remember this path. Go back? ")
        if wickery_hills == ("Yes"):
            investigate = input("Wait...This isn't the way I came from.... \n*Sound of leaves rustling.* \nWould you like to investigate the noise? ")
            if investigate == ("Yes"):
                print("You begin to approach the bushes...")
                riddle = papagnome.ask()
                print(riddle)
Roads_ForestGnome()