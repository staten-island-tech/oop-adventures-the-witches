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
SuspectList = []




def Create_Towns_Log(Name,Occupation) :
    id = str(uuid.uuid4())

    New_Villager = Townsfolks(id,Name,Occupation)
    TownsLog.append(New_Villager)
    for Townsfolk in TownsLog :
        print(Townsfolk)

def SuperSuspicious(Name,Occupation,Last_Seen):
    New_Suspect = Suspect(id,Name,Occupation,Last_Seen)
    