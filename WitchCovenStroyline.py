print("Welcome to The Witch Coven Adventure (CAPS SENSITIVE)!!! By (Nina, Hali and Serena C.)")
print("Click Terminal Box To Start")


def Witch() :
  

    # IF YOU WENT LEFT
    ChoiceOne = input("Witch Coven Adventure. It was a dark stormy evening. As a young maiden you have just finished work. Tired and annoyed of the rich family you work for, you slowly head down the wet path leading up to the hill. *You see a sign that reads* ""Left: Wickery Hills"", ""Right: ""Crystal Cliffs"". Which way do you go?")
    if ChoiceOne == "left" :
           Quest =input("You head up the path to Wickery Hills. However you dont seem to remember this path. Go back?")
          
            
           if Quest == "yes" :
               Quest2 = input("Wait...This isn't the way I came from.... *Sound of leaves rustling.* Would you like to investigate the noise?")

           if Quest2 == "yes" :
                Quest3 = input("You begin to approach the bushes. (lvl.1 FOREST GNOME DISCORVERED.) The gnome agrees to let you go if you answer his 'tricky' Riddles. (Caps sensitive) PAPA FOREST GNOME : What is seen in the middle of March and April that can't be seen at the beginning or end of either month?")
           if Quest3 == "r" :
               
               print("(GNOME DEFEATED!!!)Specimen Collected !!")
               print("Specimen Collected !!")
               print("LEVEL UP !! Lvl. 0 --> Lvl.1")
               print("Whew... That was super scary !! You begin to continue back down the path. *I hope I dont come across another gnome !*")
               Quest4 = input("You Finally Arrive At Home !!")
        #############################################################################################
           else: 
                print("Wrong Answer !")
                print("PAPA GNOME: 'KIDS!!! WE'RE EATING GOOD TONIGHT !! HOUGHHOUGHHOUGH!!")
                print("GAME OVER!")
                print("Try Again?")
                print("Run Terminal To Try again !!")
        #############################################################################################

                   

           ####################
           if Quest== "no" :
                print("Hmm. my mind seems to be wanting to play tricks on me. I'm really tired. *You continue down the rainy path.*")
        
            
           ##################
                              
        




    if ChoiceOne == "right" :
        input("You head across the bridge to Crystal cliffs. (Its such an effort to live so far and isolated away from the village. ) As it soon starts to get dark, You decide to walk faster. The thought of being in the woods this late unsettles you. You finally approach home. Would you like to shower or go to bed?")

###########################################################################################################################################################
        

Witch()

    
    