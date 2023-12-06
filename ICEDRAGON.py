class Icedragon:
    def __init__(self, name, health, personality, weapon, treasure, type):
        self.name = name
        self.health = health
        self.personality = personality
        self.weapon = weapon
        self.treasure = treasure
        self.type = type
    def battleoutcome(self, friend):
        if self.health <= 0:
            print (f"{self.name} has lost. ")
            print (f"{self.weapon} has been dropped. ")
            friendship = input (f"Befriend {self.name}?")
            if friendship == ("No"):
                print (f"{self.name} has been defeated.")
            elif friendship == ("Yes"):
                print (f"You just gained an ally! \nYou can call {self.name} to battle anytime.")
                friend.append({self.name})
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print (f"{self.name}:...")