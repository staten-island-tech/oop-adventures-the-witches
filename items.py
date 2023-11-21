import json
import os

class weapon_items:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

with open ("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here
    name = input ("name: ")
<<<<<<< Updated upstream
    desc = input ("short desc: ")

shop = weapon_items(name,desc)
=======
    desc = input ("quick desc: ")

shop = weapon_items(name, desc)
>>>>>>> Stashed changes
data.append(shop.__dict__)
print (shop.__dict__)

#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data, indent = 2)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")