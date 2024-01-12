class Maincharacter:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory
    def victory(self, items, addhealth):
        input(f"Congrats, {self.name} defeated the enemy!")
        input (f"Hooray, you gained '{items}'!")
        self.inventory.append(items)
        newhealth = self.health + addhealth
        self.health = newhealth
        return (f"Your new health is {self.health}")