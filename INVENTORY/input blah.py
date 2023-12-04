from SHOP import Seller
from TOWNSFOLK import Townfolk

Audrey = Seller("Audrey", products=["FOREST GUMP", "GOODLUCK CHARM", "DRAGON FOOD","EMERALD", "COULDRON"])
Audrey.sell("FOREST GUMP")

Vincent = Townfolk("Vincent", Occupation="Farmer", Inventory= ["Cow"])
Vincent.buy("FOREST GUMP")