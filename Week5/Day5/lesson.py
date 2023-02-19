import json

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

file_loc='family.json'
with open(file_loc,'w') as file:
    json.dump(my_family,file)