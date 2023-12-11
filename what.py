import json
import os
## Open the JSON file of pokemon data
dic = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(dic)

class moves:
  def __init__(self, ID, Move, Description, Damage):
        self.ID = ID
        self.move = Move
        self.desc = Description
        self.damage = Damage

a = input ("id:")
b = input ("move name: ")
c = input ("desc: ")
d = input ("damage: ")

a = moves(a,b,c,d)
data.append(a.__dict__)
print (a.__dict__)

new_file = "updated.json"
with open(new_file, "r") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data, indent = 3)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")