# #1
# from os import remove


# user_number = int(input('enter a number '))
# user_length = int(input('enter a length '))
# new_list = []
# for multiplied in range(1,user_length + 1):
#     new_list.append( user_number * multiplied) 
# print(new_list)

#2
user_string = input('enter a string ')
result_str = user_string[0]

for char in user_string[1:]:
    if result_str[-1] != char:
        result_str += char

print(result_str)
