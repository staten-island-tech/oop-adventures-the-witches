from merchant import Merchant
from hero import Hero
#Creates a new instance of Merchant
Audrey = Merchant("Audrey", ["Sea-Shell","green sweater","Jarvis","Soul"])
Hambergs = Hero("Amber", 500, ["Hamburger"])
item = Audrey.sell("Soul")
print(item)
Hambergs.buy (item)