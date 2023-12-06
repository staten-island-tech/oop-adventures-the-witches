import json
import os

class moves:
    def __init__(self, ID, Move, Description, Damage):
        self.ID = ID
        self.move = Move
        self.desc = Description
        self.damage = Damage

with open ("move.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here
    id = input ("id number: ")
    name = input ("name: ")
    desc = input ("short desc: ")
    dmg = input ("dmg amount: ")

a = moves(name,desc)
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
os.remove("move.json")
os.rename(new_file, "move.json")