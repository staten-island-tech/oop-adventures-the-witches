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
    for Suspect in SuspectList :
        print(Suspect)




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
        print(n) in SuspectList
        
     
         


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
  NumGuess()
  def RiddleGame1() :
     import random
     print("Welcome to four corners. You will play 3 rounds with the enemy. If you Win, you can pass. Alternatively if you loose, You die. Good luck.")
     CornerPick = input("Pick A corner (1, 2 ,3 or 4)")
     CornersAvailable = [1,2,3,4]
     Selected_Corner =random.choice(CornersAvailable)
     for i in range(3) :
        while CornerPick != Selected_Corner:
            print("Round Cleared ! The Enemy Chose ", Selected_Corner)
            

        if CornerPick == Selected_Corner:
           print("GAME OVER. The enemy chose ", Selected_Corner, "Betterm Luck Next Time...")
           break
  RiddleGame1()
       

    




