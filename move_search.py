import json
## Open the JSON file of pokemon data
pokedex = open("./move.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

user_input = input("Enter a move: ")
match_found = False

#iterating
for move in data:
    if move["move"].lower() == user_input.lower():
        match_found = True
        print(f"Move found: {move['move']} - {move['desc']}, {move['damage']}")

#checking
if not match_found:
    print("invalid")