class Seller() :
    print("Welcome to my shop !!")
    def __init__ (self,name,products) :
        self.name = name
        self.products = products
    def sell(self,item) :
        self.products.remove(item)
        print(f'you have purchased {item}')
        print("f'Here is whats left in the shop. Looking for anything else?")
        print(self.products)
    def buy(self, item) :
            self.inventory.append(item)
            print(self.inventroy)
            
            class Townfolk() :
                def __init__ (self,Name,Occupation,Are_They_A_Friend) :
                    self.Name = Name
                    self.Occupation = Occupation
                    self.Are_They_A_Friend = Are_They_A_Friend



