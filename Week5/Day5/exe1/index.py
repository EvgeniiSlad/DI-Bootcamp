import json

file_loc='file.json'
family={}

with open(file_loc, 'r') as f:
    family=json.load(f)

print(family)

# print(f'Jane`s children: {family} ')
for child in family['children']:
    print(child['firstName'])
    print(child['age'])

for child in family['children']:
    child['favorite_color']='blue'
print(family['children'])

with open(file_loc, 'w') as file:
    json.dump(family,file,indent=4)


