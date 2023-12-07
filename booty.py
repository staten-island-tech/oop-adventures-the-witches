import json
import os

class moves:
    def __init__(self, ID, Enemy, Move, Description, Damage):
        self.ID = ID
        self.Enemy = Enemy
        self.Move = Move
        self.Description = Description
        self.Damage = Damage

with open ("moves.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here
    id = input ("id number: ")
    enemy = input ("which enemy can learn this move?: ")
    move = input ("move name: ")
    desc = input ("short desc: ")
    dmg = input ("dmg amount: ")

a = moves(id, enemy, move, desc, dmg)
data.append(a.__dict__)
print (a.__dict__)

#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data, indent = 3)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("moves.json")
os.rename(new_file, "moves.json")