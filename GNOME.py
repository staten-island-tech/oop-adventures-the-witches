class Forestgnome:
    def __init__(self, name, health, riddle, riddleanswer, chances, weapon):
        self.name = name
        self.health = health
        self.riddle = riddle
        self.riddleanswer = riddleanswer
        self.chances = chances
        self.weapon = weapon
    def ask(self):
        riddle = input(f"{self.name}: {self.riddle}")
        if riddle == self.riddleanswer:
            self.health = 0
            return (f"{self.name}: NOOOO!!! No one has ever answered correctly before!!")
        elif riddle != self.riddleanswer:
            return ("Be prepared for battle!!!")
    def battleresult(self):
        if self.health <= 0:
            print (f"{self.name} has been defeated.")
            return (f"{self.weapon} was dropped.")
        elif self.health > 0:
            print (f"{self.name} won the battle!")
            return (f"{self.name}: Haha, I knew I would win!!")