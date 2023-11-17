import json
import os
## Create Class for creating new dictionaries here

class Character:
    def __init__(self, name, level, vision, weapon):
        self.name = name
        self.level = level
        self.vision = vision
        self.weapon = weapon

with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

a = input('name: ')
b = input('level: ')
c = input('vision: ')
d = input('weapon: ')

class f:
    def __init__(self, filename):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)
                
data.append({
            'name': a,
            'level': b,
            'vision': c,
            'weapon': d
        })



#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")