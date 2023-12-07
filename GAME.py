def Roads():
    roadsChoice = input("It was a dark stormy evening. As a young maiden you have just finished work. Tired and annoyed of the rich family you work for, you slowly head down the wet path leading up to the hill. You see a sign that reads 'Left: Wickery Hills', 'Right: Crystal Cliffs'. Which way do you go?")
    if roadsChoice == ("Left"):
        from GNOME import Forestgnome
        papagnome = Forestgnome("Papa Forest Gnome", 250, "What is seen in the middle of March and April that can't be seen at the beginning or end of either month?", "r", 3, "")
        wickery_hills = input("You head up the path towards Wickery Hills. However you dont seem to remember this path. Go back?")
        if wickery_hills == ("Yes"):
            investigate = input("Wait...This isn't the way I came from.... *Sound of leaves rustling.* Would you like to investigate the noise?")
            if investigate == ("Yes"):