# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict["class"]["student"]["marks"]["history"])

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# keys_to_remove = ["name", "salary"]
# for key in keys_to_remove:
#     del sample_dict[key]  
# print(sample_dict)



birthdays={"Zhenia" : "1999/01/07",
            "Ira" : "2001/21/08",
            "Sasha" : "1999/19/01",
            "Jenia" : "2001/04/01",
            "Dima" : "2001/06/02"
}
print("You can look up the birthdays of the people in the list!")
name=input("Write the name:")
# birthday = birthdays[name]
birthday = birthdays.get(name,f"THERE is no {name} in the data ")
print(birthday)