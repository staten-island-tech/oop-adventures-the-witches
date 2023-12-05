

class battle:
    def __init__(self, name, opponent, weapon, move, hp, enemy_hp):
        self.name = name
        self.opponent = opponent
        self.weapon= weapon
        self.move = move
        self.hp = hp
        self.enempy_hp = enemy_hp

##initiating battle
print("Encountered wild o, engage in battle? (Y/N)")
#put hero class when its done
if input == "Y":
    print("Engaging into battle")
elif input == "N":
    print("Ran away successfully")
else:
    print("invalid")

#what u do in turns       
print("What would you like to do? Fight/Use items")
if input == "Fight":
    print("Select a move:" )
elif input == "Use items":
    print("Select item you want to be used: ")
else: 
    print("invalid")
    
##turns
    


        


##if enemy.hp <= 0:
    ##print("You won")
##elif hero.hp <= 0:
    ##print("You lost")


