

def RiddleGame1() :
     import random
     print("Welcome to four corners. You will play 3 rounds with the enemy. If you Win, you can pass. Alternatively if you loose, You die. Good luck.")

     CornersAvailable = [1,2,3,4]
   
     Rounds = 3
     for i in range(3):
        Selected_Corner =random.choice(CornersAvailable)
        CornerPick = input("Pick A corner (1, 2 ,3 or 4)") 
        if CornerPick == Selected_Corner:
               print("GAME OVER! The enemy chose corner number:", Selected_Corner, ". You chose Corner number:", CornerPick)
               break
          
        elif CornerPick != Selected_Corner:
               while Rounds != 0 :
                print("ROUND CLEAR !The enemy chose corner     number:", Selected_Corner, ". You chose Corner number:", CornerPick)
                Rounds -=1
                if Rounds == 0:
                    print("Well done. GAME CLEAR.")

     







def RiddleGame2() :
     print("Welcome to Rock, Paper, Scissors. Best of 3 WINS. Loser dies.")

     import random
     RPS = ["ROCK", "PAPER", "SCISSORS"]
     RoundCount = 0
     ScoreCount = 0
     EnemyScoreCount = 0
     while RoundCount < 4 :
       for i in range(3):
          YourRPS = input("Please choose Rock, Paper, Or Scissors.")
          print(YourRPS.upper())
          EnemyRPS = random.choice(RPS)
          print("The enemy chose ", EnemyRPS)
          if YourRPS.upper() == "ROCK" and EnemyRPS == "ROCK":
              print("DRAW ! You BOTH picked rock.")
              RoundCount +=1
              ##
          elif YourRPS.upper() == "SCISSORS" and EnemyRPS == "SCISSORS" :
              print("DRAW ! You BOTH picked scissors.")
              RoundCount +=1
              ##
          elif YourRPS.upper() == "PAPER" and EnemyRPS == "PAPER" :
              print("DRAW! You BOTH picked scissors.")
              RoundCount +=1
              ##
          elif YourRPS.upper() == "PAPER" and EnemyRPS == "SCISSORS" :
              print("ENEMY WINS !. Scisssors beats paper.")
              RoundCount +=1    
              EnemyScoreCount +=1
              ##
          elif YourRPS.upper() == "ROCK" and EnemyRPS == "PAPER" :
              print("YOU get a point! Rock beats paper.")
              RoundCount +=1  
              ScoreCount +=1
              ##       
          elif YourRPS.upper() == "ROCK" and EnemyRPS == "SCISSORS" :
              print("YOU get a point! Rock beats scissors!")
              RoundCount +=1
              ScoreCount +=1
              ##
          elif YourRPS.upper() == "SCISSORS" and EnemyRPS == "ROCK" :
              print("ENEMY GETS A POINT! Rock BEATS scissors!")
              RoundCount +=1
              EnemyScoreCount +=1
              ##
          elif YourRPS.upper() == "SCISSORS" and EnemyRPS == "PAPER" :
              print("You get a point! Scissors BEATS paper!")
              RoundCount +=1
              ScoreCount +=1
          else :
              print("Something went wrong. Are you sure you typed that correctly?(REPLAY BY RECLICKING TERMINAL)")
              break
         
       if RoundCount ==3 and ScoreCount > EnemyScoreCount:
           print("You're score is", ScoreCount)
           print("The ENEMY'S score is", EnemyScoreCount)
           print("YOU WIN!")
           break
       if RoundCount ==3 and ScoreCount < EnemyScoreCount:
           print("You're score is", ScoreCount)
           print("The ENEMY'S score is", EnemyScoreCount)
           print("YOU LOST!. Game Over...") 
           break
       if RoundCount ==3 and ScoreCount == EnemyScoreCount :
           print("You're score is", ScoreCount)
           print("The ENEMY'S score is", EnemyScoreCount)
           print("Its....A tie.....")         
     

     
RiddleGame2()



                

            

     


def BombDefusion() :
    WIRES = ["RED","GREEN","BLUE","YELLOW"]
    print("There are 4 wires. RED, YELLOW , GREEN, OR BLUE.")
    print("Objective: Cut the correct wire in order to stop the bomb.")
    print("Each round the correct wire regenerates. Meaning that this game is based off of pure luck.")
    chances = 3
    import random
    print("You Currently have", chances, "Chances. Goodluck.")

    while chances > 0 :
            for i in range(3) :
                YourWireCut = input("Which Color Wire Would You Like To Cut? RED, YELLOW, GREEN, OR BLUE?")
                Correct_Wire = random.choice(WIRES)
                if YourWireCut != "RED".lower() or "YELLOW".lower() or "GREEN".lower() or "BLUE".lower():
                    print("Something went wrong. Are you sure you typed that correctly? Im gonna have to take away a chance for that one buddy.")
                    print("You have", chances, "Chances left")
                if YourWireCut == Correct_Wire :
                    print("Well Done!", YourWireCut,"Was the correct choice")
                    break
                if YourWireCut != Correct_Wire :
                    print("Guess Again!", YourWireCut, "Is not correct.")
                    chances -=1
                    print("You have", chances, "Chances left. Goodluck.")
                if chances == 0 :
                    print("GAME OVER! You Ran out of tries.")
                    print("You have failed to defuse the bomb.")
BombDefusion()


def RussianRoulette() :
    import random
    REVOLVER = [1,2,3,4,5,6]
    AmountOfBullets = random.choice(3)(REVOLVER)
    print(AmountOfBullets)
RussianRoulette()