class Townsfolks :
    def __init__(self,id,Name,Occupation) :
   
        self.Name = Name
        self.Occupation = Occupation
        self.id = id


class Suspect(Townsfolks) :
    def __init__(self,id,Name,Occupation, Last_Seen) : 
        super().__init__(id,Name,Occupation)
        self.Last_Seen = Last_Seen
    def __str__(self):
        return f"{self.Name},{self.Occupation},{self.Last_Seen}"
   
test = Suspect(4,"Test", "asdf","sdfg")

print(test)