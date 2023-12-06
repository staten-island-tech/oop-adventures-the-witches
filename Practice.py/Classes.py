import uuid


print("Welcome to your persnal Journal. Here you will record your suspiciouns abt others")
class Guest :
    def __init__(self,Name,Occupation) :
        self.Name = Name
        self.Occupation = Occupation


""" new_id = str(uuid.uuid4())
mark = User(new_id, "Mark") ##new instance of User
print(mark) """




class GuestInfo :
    def __init__(self, Name, Occupation, Relation_To_You, Relation_To_Mansion_owner):
        super().__init__(Name,Occupation)
        self.Relation_To_You = Relation_To_You
        self.Relation_To_Mansion_owner = Relation_To_Mansion_owner
       




class Suspicions(Guest) :
    def __init__(self,Name,Occupation,Reason_For_Suspicion,Last_Seen_With,Relation_To_You) :
         super().__init__(Occupation,Name,Relation_To_You)
     
         self.Reason_For_Suspicion = Reason_For_Suspicion
         self.Last_Seen_With = Last_Seen_With
    def __str__(self):
        return f"{self.Name},{self.Occupation},{self.Relation_To_You}"
       




class NotSuspicious(Guest) :
    def __init__(self,Name,Occupation, ReasonOfTrust,Befriend) :
        super().__init__(self,Name,Occupation)
        self.ReasonOfTrust = ReasonOfTrust
        self.Befriend = Befriend


Guests =[]
SuspectList =[]
Trusts =[]




def Create_Guest_Log(Name, Occupation,Relation_To_Mansion_owner):
    Occupation = (uuid.uuid4())
    A_Guest = Guest(Name,Occupation,Relation_To_Mansion_owner)
    Guests.append(A_Guest)
    for Guest in Guests:
        print(Guest)






def Create_Suspicions(Name,Occupation,Relation_To_Mansion_owner,Reason_For_Suspicion) :
    Occupation = (uuid.uuid4())
    Suspect = Suspicions(Name,Occupation,Relation_To_Mansion_owner,Reason_For_Suspicion)
    SuspectList.append(Suspect)
    for Suspect in SuspectList :
        print(Suspect)


def Create_Trustworthy(Name,Occupation,Relation_To_Mansion_owner,ReasonOfTrust,Befriend) :
    Occupation = (uuid.uuid4())
    Trust = NotSuspicious(Name,Occupation,Relation_To_Mansion_owner,ReasonOfTrust,Befriend)
    Trusts.append(Trust)
    for Trust in Trusts :
        print(Trust)






add_users_Guest_Log ="Y"
def check_tenure(status):
    if status.lower() == "y" :
        return True
    else :
        return False
   


while add_users_Guest_Log == "Y" :
    print("Welcome to the journal. Here you will recod all of your findings on the locals.")
    User_Request = input("Before you Input information on this character, Are you Suspicious of Him/Her?(YES or NO or UNDETERMINED)")
    if User_Request.upper() == "YES" :
        print("Classing into Suspicions file...")
        name = input("Enter A Guest Name.")
        Occupation = input("Please Enter This Guest's Occupation. (Just put a '?' If its unkown.)")
        LastSeenWith = input("Please State Where you last saw this person ")
        RelationToU = input("What is this person's relation to you? Leave a '?' If its unkown.")
        ReasonForSuspicion = input("Please State in 1-2 EXTREMELY short sentences your reason for suspicion.")


        Create_Suspicions(name,Occupation,ReasonForSuspicion,LastSeenWith,RelationToU)
