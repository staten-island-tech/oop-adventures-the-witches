class Forestgnome:
    def __init__(self, name, personality, riddle, riddleanswer, chances, weapon):
        self.name = name
        self.personality = personality
        self.riddle = riddle
        self.riddleanswer = riddleanswer
        self.chances = chances
        self.weapon = weapon
    def ask(self):
        riddle = input(self.riddle)
        if riddle == self.riddleanswer:
            print ("NOOOO!!! No one has ever answered correctly before!!")
            print (f"{self.name} has been defeated.")
        elif riddle != self.riddleanswer:
            print ("Be prepared for battle!!!")
    def battle(self, defeat, victory):
        print ("")