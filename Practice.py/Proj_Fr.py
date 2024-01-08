import uuid


A = input("This is your journal. Here you will keep a log of the townsfolk. This will help you identify whos the which faster. ")




class Townsfolks :
    def __init__(self,id,Name,Occupation) :
   
        self.Name = Name
        self.Occupation = Occupation
        self.id = id


"""new_id = str(uuid.uuid4())
mark = User(new_id, "Mark") ##new instance of User
print(mark)"""








class Suspect(Townsfolks) :
    def __init__(self,id,Name,Occupation, Last_Seen) : 
        super().__init__(id,Name,Occupation)
        self.Last_Seen = Last_Seen
    def __str__(self):
        return f"{self.Name},{self.Occupation},{self.Last_Seen}"


TownsLog =[]
SuspectList =[]




def Create_Towns_Log(Name, Occupation) :
    id = str(uuid.uuid4())




    New_Villager = Townsfolks(id,Name,Occupation)
    TownsLog.append(New_Villager)
    for Townsfolk in TownsLog :
        print(Townsfolk)


def Sussy(Name,Occupation,Last_Seen) :
    New_Suspect = Suspect(id,Name,Occupation,Last_Seen)
    SuspectList.append(New_Suspect)
   




add_more_users = "Y"
def check_tenure(status):
    if status.lower() == "y":
        return True
    else:
        return False
   
while add_more_users == "Y":
    user_request = input("Welcome to your Journal log. What Will You Write About( Suspect or Townsfolk.)?")
    if user_request== "Townsfolk":
        Name = input("Enter Name Of Person")
        Occupation = input("Please Enter Occupation Of TownsFolk")
        Create_Towns_Log(Name,Occupation)        
   
   
   

    elif user_request == "Suspect" :
        Name = input("Enter Name Of Person")
        Occupation = input("Please Enter Occupation Of TownsFolk")
        Last_Seen = input("Where was this person last seen?")
        n = Suspect(1,Name,Occupation,Last_Seen)
        SuspectList.append(n)
        print(SuspectList[0])

        
     
         


    else:
        print("Soemthing went wrong, are you sure you typed the request correctly? Imagine not being able to spell   ") 
    add_more_users = input("Would you like to continue Y/N ").upper()
    if add_more_users == "N" :
            break 
    
def Journal_check():
 Journal =input("Welcome to your journal ! What would you like to see?(Townsfolk or Suspects)")

 if Journal == "TownsFolk" :
    print(TownsLog)

 elif Journal == "Suspects" :
    print(SuspectList)


Journal_check()



class Minigames() :
  
  def NumGuess() :
    import random
    print("Im Thinking Of A Number Between 1 And 10. You have 3 Tries to guess !")
    number = random.randint (1,10) 
    
    for chances in range(3) :
      guess = int(input("Guess A Number!"))
    
      if guess == number:
         print("You got it!The number was RIGHT!")
         break
      

      elif guess > number:
       print("Wrong! Try a little lOWER. ")

      if guess < number :
       print("Wrong! Try a little higher.")

def RPS() :
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

def FourCorners() :
     
     import random
     print("Welcome to four corners. You will play 3 rounds with the enemy. If you Win, you can pass. Alternatively if you loose, You die. Good luck.")
     CornersAvailable = [1,2,3,4]
     Rounds = 3
     
     while Rounds > 0 :
        for i in range(3):
            YourFC = int(input("Please Choose A Corner (1,2,3 or 4)"))
            print("You Chose corner number ", YourFC)
            EnemyFC = random.choice(CornersAvailable)

            if YourFC == EnemyFC :
             print("The Enemy Also Chose Corner", EnemyFC)
             print("GAME OVER!")
             Rounds -=3
            elif YourFC != EnemyFC :
               Rounds -=1
               print("The Enemy Chose Corner", EnemyFC, ".")
               print("Round Clear!" , Rounds, "Rounds Left") 
               print("CLEAR !")

def BombDefusion() :
    WIRES = ["RED","GREEN","BLUE","YELLOW"]
    print("There are 4 wires. RED, YELLOW , GREEN, OR BLUE.")
    print("Objective: Cut the correct wire in order to stop the bomb.")
    print("Each round the correct wire regenerates. Meaning that this game is based off of pure luck.")
    chances = 3
    import random
    print("You Currently have", chances, "Chances. Goodluck.")
    while chances < 0 :
        Correct_Wire = random.choice(WIRES)
        YourWireCut = input("Which Color Wire Would You Like To Cut? RED, YELLOW, GREEN, OR BLUE")
        if YourWireCut != "RED" or "YELLOW" or "GREEN" or "BLUE":
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
        



       

    




