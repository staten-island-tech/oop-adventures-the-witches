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
        newhealth = self.health + 1,000
        self.health.replace(self.health, newhealth)
        print (f"Your new health is {newhealth}")
    def defeat(self):
        print ("Nooo, you didn't defeat the enemy!")
        newhealth = self.health - 500
        self.health.replace(self.health, newhealth)
        print (f"Your new health is {newhealth}")
    def newweapon(self, items):
        weapon = input(f"Whats this? Theres a new weapon! Do you wish to pick up {items}? ")
        if weapon == ("No"):
            print ("Okay then...")
        elif weapon == ("Yes"):
            self.inventory.append(items)
            print ("Item added to inventory.")