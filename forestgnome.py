class Forestgnome:
    def __init__(self, name, personality, riddle, chances):
        self.name = name
        self.personality = personality
        self.riddle = riddle
        self.chances = chances
<<<<<<< Updated upstream
    def chances(self, item):
        self.chances.remove(item)
=======
    def answer(self):
        self.chances.remove(self.chances[-1])
>>>>>>> Stashed changes
        print (f"You have {self.chances} left!!!")

