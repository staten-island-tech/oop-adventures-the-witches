class Maincharacter:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory
    def victory(self, items):
        print("Congrats, you defeated the enemy!")
        self.inventory.append(items)
        print ("Hooray, you got more items!")
        newhealth = self.health + 500
        self.health = newhealth
        return (f"Your new health is {self.health}")
    def defeat(self):
        print ("Nooo, you didn't defeat the enemy!")
        newhealth = self.health - 500
        self.health = newhealth
        if self.health < 0:
            self.health = 0
        return (f"Your new health is {self.health}")
    def newweapon(self, items):
        weapon = input(f"Whats this? Theres a new weapon! Do you wish to pick up {items}? ")
        if weapon == ("No"):
            return ("Okay then...")
        elif weapon == ("Yes"):
            self.inventory.append(items)
            return ("Item added to inventory.")