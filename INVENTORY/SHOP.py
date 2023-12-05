class Seller() :
    print("Welcome to my shop !!")
    def __init__ (self,name,products,inventory) :
        self.name = name
        self.products = products
  
    def buy(self,item) :
        self.products.remove(item)
        print(f'you have purchased {item}')
        print("f'Here is whats left in the shop. Looking for anything else?")
        print(self.products)
    def sell(self, item) :
            self.inventory.append(item)
            print(self.inventory)
            
class Townfolk() :
    def __init__ (self,Name,Occupation,Are_They_A_Friend,Inventory) :
        self.Name = Name
        self.Occupation = Occupation
        self.Are_They_A_Friend = Are_They_A_Friend
        self.Inventory = Inventory
        

Audrey = Seller("Audrey", products=["FOREST GUMP", "GOODLUCK CHARM", "DRAGON FOOD","EMERALD", "COULDRON"])
Audrey.sell("FOREST GUMP")

Vincent = Townfolk("Vincent", Occupation="Farmer", Inventory= ["Cow"])
Vincent.buy("FOREST GUMP")




Charlotte = Townfolk("Charlotte", Occupation="Town Crazy", Inventory= ["?"])

Leila = Townfolk(Name="Leila", Occupation="Church Worker", Inventory= ["Spiritual Items"])

Victor= Townfolk(Name="Victor", Occupation="Village Head", Inventory= ["?"])

Tristan = Townfolk(Name="Tristan", Occupation="Maid", Inventory= ["Broom","Dustpan","6 Coins","Basket","Master's Bedroom Key","Suite Key","Balcony Key"])


data = Townfolk
print(Townfolk.Name)

