
from SHOP import Seller
class Townfolk() :
    def __init__ (self,Name,Occupation,Are_They_A_Friend) :
        self.Name = Name
        self.Occupation = Occupation
        self.Are_They_A_Friend = Are_They_A_Friend
        def buy(self, item) :
            self.inventory.append(item)
            print(self.inventroy)


        
