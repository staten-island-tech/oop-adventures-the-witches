import uuid

print("This is your journal. Here you will keep a log of the townsfolk. This will help you identify whos the which faster. ")


class Townsfolks :
    def __init__(self,id,Name,Occupation) :
    
        self.Name = Name
        self.Occupation = Occupation
        self.id = id

"""new_id = str(uuid.uuid4())
mark = User(new_id, "Mark") ##new instance of User
print(mark)"""




class Suspect(Townsfolks) :
    def init__(self,id,Name,Occupation, Last_Seen) :
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




    
while add_more_users == "Y":
    user_request = input("Welcome to your Journal log. What Will You Write About( Suspect or Townsfolk.)?")
    if user_request.upper() == "Townsfolk":
        Name = input("Enter Name Of Person")
        Occupation = input("Please Enter Occupation Of TownsFolk")
        Create_Towns_Log(Name,Occupation)        

    
