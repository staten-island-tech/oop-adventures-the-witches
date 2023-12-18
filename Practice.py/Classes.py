
# import uuid


# print("Welcome to your persnal Journal. Here you will record your suspiciouns abt others")
# class Guest :
#     def __init__(self,Name,Occupation) :
#         self.Name = Name
#         self.Occupation = Occupation


# """ new_id = str(uuid.uuid4())
# mark = User(new_id, "Mark") ##new instance of User
# print(mark) """



       




# class Suspicions(Guest) :
#     def __init__(self,Name,Occupation,Reason_For_Suspicion,Last_Seen_With,Relation_To_U) :
#          super().__init__(Occupation,Name,Relation_To_U)
     
#          self.Reason_For_Suspicion = Reason_For_Suspicion
#          self.Last_Seen_With = Last_Seen_With
#     def __str__(self):
#         return f"{self.Name},{self.Occupation},{self.Relation_To_U}"
       




# class NotSuspicious(Guest) :
#     def __init__(self,Name,Occupation, ReasonOfTrust,Befriend) :
#         super().__init__(self,Name,Occupation)
#         self.ReasonOfTrust = ReasonOfTrust
#         self.Befriend = Befriend


# Guests =[]
# SuspicionS =[]
# NotSuspiciousS =[]




# def Create_Guest_Log(Name, Occupation,Relation_To_U):
#     Occupation = (uuid.uuid4())
#     A_Guest = Guest(Name,Occupation,Relation_To_U)
#     Guests.append(A_Guest)
#     for Guest in Guests:
#         print(Guest)






# def Create_Suspicions(Name,Occupation,Relation_To_Mansion_owner,Reason_For_Suspicion) :
#     Occupation = (uuid.uuid4())
#     Suspect = Suspicions(Name,Occupation,Relation_To_Mansion_owner,Reason_For_Suspicion)
#     SuspicionS.append(Suspect)
#     for Suspect in SuspicionS :
#         print(Suspect)


# def Create_Trustworthy(Name,Occupation,Relation_To_U,ReasonOfTrust,Befriend) :
#     Occupation = (uuid.uuid4())
#     Trust = NotSuspicious(Name,Occupation,Relation_To_U,ReasonOfTrust,Befriend)
#     NotSuspiciousS.append(Trust)
#     for Trust in NotSuspiciousS :
#         print("Here Is your Current Suspicions")
#         print(Trust)






# add_users_Guest_Log ="Y"
# def check_tenure(status):
#     if status.lower() == "y" :
#         return True
#     else :
#         return False
   


# while add_users_Guest_Log == "Y" :
#     print("Welcome to the journal. Here you will recod all of your findings on the locals.")
#     User_Request = input("Before you Input information on this character, Are you Suspicious of Him/Her?(YES or NO or UNDETERMINED)")
    
#     if User_Request.upper() == "YES" :
#         print("Classing into Suspicions file...")
#         Name = input("Enter A Guest Name.")
#         Occupation = input("Please Enter This Guest's Occupation. (Just put a '?' If its unkown.)")
#         LastSeenWith = input("Please State Where you last saw this person ")
#         Relation_To_Mansion_owner= input("What is this person's relation to the mansion owner? Leave a '?' If its unkown.")
#         Reason_For_Suspicion = input("Please State in 1-2 EXTREMELY short sentences your reason for suspicion.")

        
#         Create_Suspicions(Name,Occupation,Relation_To_Mansion_owner,Reason_For_Suspicion) 
# ###############################################################
#     elif User_Request.upper() =="UNDETERMINED" :
#         print("Redirecting To Regular Guest Log...")
#         Name = input("Enter A Guest Name.")
#         Occupation = input("Please Enter This Guest's Occupation. (Just put a '?' If its unkown.)")
#         Relation_To_U = input("What is this person's relation to you? Leave a '?' If its unkown.")
                                            
# ###############################################################
        
#     elif User_Request.upper() == "NO" :
#         print("Redirecting to the list of trustworthy people....")
#         Name = input("Enter A Guest Name.")
#         Occupation = input("Please Enter This Guest's Occupation. (Just put a '?' If its unkown.)")
       
# ###################################################################




