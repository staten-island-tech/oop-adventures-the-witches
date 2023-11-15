import json
import os

##Class for enemies:

class ENEMIES:
    def __init__(self, height, power, strength, attack_moves, appearance):
        self.height = height
        self.power = power
        self.strength = strength
        self.attack_moves = attack_moves
        self.appearance = appearance

with open ("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here
    height = input ("Name an enemy's height: ")
    power = input ("Name your enemy's power element: ")
    strength = input ("Name your enemy's physical strength level: ")
    attack_moves = input ("Name the attack moves your enemy can do: ")
    appearance = input ("Name significant physical appearances of your enemy: ")
    personality = input ("Name your enemy's personality: ")
