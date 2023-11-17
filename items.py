import json
import os

with open("move.json", "r") as f:
    data = json.load(f)

class items:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __init__(self):
        return f"{self.name} {self.description}"


input("name: ")
input("desc: ")


new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)
    f.write(json_string)

os.remove("move.json")
os.rename(new_file, "move.json")