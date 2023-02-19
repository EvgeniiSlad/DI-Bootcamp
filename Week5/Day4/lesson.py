file_location1 = '/Users/evgeniisladkov/Desktop/DI-Bootcamp/Week5/Day4/files/files.txt'
file_text = ""
with open(file_location1, 'r') as f:
    file_text = f.read()
# print(file_text)


file1=''
with open(file_location1, 'r') as f:
    file1=f.readlines()
    lines5= file1[:5]
# print(lines5)

file2=''
with open(file_location1, 'r') as f:
    file2=list(f.read())
    char5=file2[0:5]
print(char5)

file3=[]
with open(file_location1,'r') as f:
    file3=f.readlines()

print(file3)
