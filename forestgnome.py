class Forestgnome:
    def __init__(self, name, personality, riddle, chances):
        self.name = name
        self.personality = personality
        self.riddle = riddle
        self.chances = chances
    def chances(self, item):
        self.chances.remove(item)
        print (f"You have {self.chances} left!!!")

