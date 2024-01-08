import uuid


A = input("This is the journal. Here you will keep a log of all townsfolk and record any suspicions.")
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
SuspectList = [Suspect]




def Create_Towns_Log(Name,Occupation) :
    id = str(uuid.uuid4())

    New_Villager = Townsfolks(id,Name,Occupation)
    TownsLog.append(New_Villager)
    for Townsfolk in TownsLog :
        print(Townsfolk)

def SuperSuspicious(Name,Occupation,Last_Seen):
    New_Suspect = Suspect(id,Name,Occupation,Last_Seen)
    SuspectList.append(New_Suspect)
    for Suspect in SuspectList :
        print(New_Suspect)
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
        print (SuspectList)

    else:
        print("Soemthing went wrong, are you sure you typed the request correctly? Imagine not being able to spell   ") 
    add_more_users = input("Would you like to continue Y/N ").upper()
    if add_more_users == "N" :
         break 

    def JournalCheck() :
        JournalView = input("Welcome To Journal. What would you like to see? (Suspects of Townsfolk?)")
        if JournalView == "Townsfolks":
            print(TownsLog)
        elif JournalView == "Suspects" :
            print(SuspectList)
        else:
            print("Are you Sure you spelled that correctly?)")
JournalCheck()