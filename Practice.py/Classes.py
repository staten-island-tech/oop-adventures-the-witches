print("Welcome to your persnal Journal. Here you will record your suspiciouns abt others")



class Guest :
    def __init__(self, Name, Occupation, Relation_To_You, Relation_To_Mansion_owner):
        self.Name = Name
        self.Occupation = Occupation
        self.Relation_To_You = Relation_To_You
        self.Relation_To_Mansion_owner = Relation_To_Mansion_owner
       

class Journal(Guest) :
    def __init__(self,Name,Occupation,Reason_For_Suspicion,Last_Seen_With) :
         super().__init__(Occupation,Name)
      
         self.Reason_For_Suspicion = Reason_For_Suspicion
         self.Last_Seen_With = Last_Seen_With
    def __str__(self):
        return f"{self.Name},{self.Occupation}"
        

