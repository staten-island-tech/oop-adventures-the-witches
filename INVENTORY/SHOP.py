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