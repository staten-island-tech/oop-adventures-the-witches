from SHOP import Seller
from TOWNSFOLK import Townfolk

Vincent = Seller("Vincent",["FOREST GUMP","GOODLUCK CHARM", "DRAGON FOOD","EMERALD", "COULDRON","DISGUISE"])
Tillary = Townfolk("Tillary","Maid","No")
item = Vincent.sell("EMERALD")
print(item)
Tillary.buy(item)
