import json
import os

#Class for enemies:
class ENEMIES:
    def __init__(self, name, height, power, strength, attack_moves, desc, personality, health):
        self.name = name
        self.height = height
        self.power = power
        self.strength = strength
        self.attack_moves = attack_moves
        self.desc = desc
        self.personality = personality
        self.health = health

with open ("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here
    name = input ("Who is the enemy? ")
    height = input ("Name an enemy's height: ")
    power = input ("Name your enemy's power/element: ")
    strength = input ("Name your enemy's physical strength level: ")
    attack_moves = input ("Name the attack moves your enemy can do: ")
    desc = input ("Name significant physical appearances of your enemy: ")
    personality = input ("Name your enemy's personality: ")
    health = input ("Name your enemy's health: ")

villains = ENEMIES(name, height, power, strength, attack_moves, desc, personality, health)
data.append(villains.__dict__)
print (villains.__dict__)

#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data, indent = 5)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")