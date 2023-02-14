users_input = 'without,hello,bag,world'
users_input_list = users_input.split(',')
sorted_users_input_list = sorted(users_input_list)
sorted_users_input = ','.join(sorted_users_input_list)
print(sorted_users_input)