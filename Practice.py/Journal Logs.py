
def RiddleGame1() :
     import random
     print("Welcome to four corners. You will play 3 rounds with the enemy. If you Win, you can pass. Alternatively if you loose, You die. Good luck.")

     CornersAvailable = [1,2,3,4]
   
     Rounds = 3
     for i in range(3):
        CornerPick = input("Pick A corner (1, 2 ,3 or 4)")
        Selected_Corner =random.choice(CornersAvailable)
        if CornerPick == Selected_Corner:
               print("GAME OVER! The enemy chose corner number:", Selected_Corner, ". You chose Corner number:", CornerPick)
               break
          
        elif CornerPick != Selected_Corner:
               while Rounds != 0 :
                print("ROUND CLEAR !The enemy chose corner number:", Selected_Corner, ". You chose Corner number:", CornerPick)
                Rounds -=1
                if Rounds == 0:
                    print("Well done. GAME CLEAR.")

     
RiddleGame1()









