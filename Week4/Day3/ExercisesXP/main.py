#1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# list1 :dict = dict(zip(keys,values))
# print(list1)

#2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# cost=0
# for age in family.values():
#     if 12>=age>3:
#         cost+=10
#     elif age>12:
#         cost+=15
# print(cost)

#3
# brand={
#     "name": "Zara" ,
#     "creation_date": 1975,
#     "creator_name": {"Amancio Ortega Gaona "},
#     "type_of_clothes":{" men, women, children, home "},
#     "international_competitors": {"Gap, H&M, Benetton "},
#     "number_stores": 7000 ,
#     "major_color":{ 
#         "France": "blue", 
#         "Spain": "red", 
#         "US": {"pink, green"}
#         }
# }
# brand["number_stores"]=2
# # print(brand["number_stores"])
# types=brand["type_of_clothes"]
# clients="Zara client are:"
# for i in types:
#     clients+=i+" "
# # print(clients)
# country=brand.update({"country_creation":"Spain"})

# if 'international_competitors' in brand:
#     brand['international_competitors']='Desigual'


# brand.pop('creation_date')

# print(brand['international_competitors'][-1])

# print(brand['major_color']['US'])

# print(len(brand))

# print(brand.keys())

# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
# }
# brand.update(more_on_zara)
# print(brand)

# print(brand['number_stores'])

#4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}
for i in users:
    disney_users_A[i] = users.index(i)
print(disney_users_A)

disney_users_B = {}
for i in users:
    disney_users_B[users.index(i)] = i
print(disney_users_B)

disney_users_C = {}
users=sorted(users)
for i in users:
    disney_users_C[i] = users.index(i)
print(disney_users_C)