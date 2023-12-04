class Forestgnome:
    def __init__(self, name, health, personality, riddle, riddleanswer, chances, weapon):
        self.name = name
        self.health = health
        self.personality = personality
        self.riddle = riddle
        self.riddleanswer = riddleanswer
        self.chances = chances
        self.weapon = weapon
    def ask(self):
        riddle = input(f"{self.name}: {self.riddle}")
        if riddle == self.riddleanswer:
            print (f"{self.name}: NOOOO!!! No one has ever answered correctly before!!")
            print (f"{self.name} has been defeated.")
            self.health.replace(self.health, 0)
        elif riddle != self.riddleanswer:
            print ("Be prepared for battle!!!")
    def battleresult(self):
        if self.health <= 0:
            print (f"{self.name} has been defeated.")
            print (f"{self.weapon} was dropped.")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            print (f"{self.name}: Haha, I knew I would win!!")