class Maincharacter:
    def __init__(self, name, height, power, health, strength, attackmoves, desc, inventory):
        self.name = name
        self.height = height
        self.power = power
        self.health = health
        self.strength = strength
        self.attackmoves = attackmoves
        self.desc = desc
        self.inventory = inventory
    def victory(self, items):
        print("Congrats, you defeated the enemy!")
        self.inventory.append(items)
        print ("Hooray, you got more items!")
        print (f"New health: {self.health + 1,000}")
