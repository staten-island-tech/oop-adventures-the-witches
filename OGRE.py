class Ogre:
    def __init__(self, name, health, personality, weapon):
        self.name = name
        self.health = health
        self.personality = personality
        self.weapon = weapon
    def battleoutcome(self):
        if self.health <= 0:
            print (f"{self.name} has been defeated. ")
            print (f"{self.weapon} has been dropped. ")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print (f"{self.name}: HAHAHAHAHA")