class Maincharacter:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory
    def victory(self, items):
        print(f"Congrats, {self.name} defeated the enemy!")
        self.inventory.append(items)
        print (f"Hooray, you gained '{items}'!")
        self.inventory.append(items)
        newhealth = self.health + 500
        self.health = newhealth
        return (f"Your new health is {self.health}")
    def defeat(self):
        print (f"Nooo, {self.name} didn't defeat the enemy!")
        newhealth = self.health - 500
        self.health = newhealth
        if self.health < 0:
            self.health = 0
        return (f"Your new health is {self.health}")
    def pickup(self, items):
        weapon = input(f"Whats this? Do you wish to pick up {items}? ")
        if weapon == ("No"):
            return ("Okay then...")
        elif weapon == ("Yes"):
            self.inventory.append(items)
            return ("Item added to inventory.")