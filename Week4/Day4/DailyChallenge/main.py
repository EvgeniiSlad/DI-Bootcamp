from curses.ascii import isalpha


matrix = [
    [7, 'i', 3],
    ['T', 's', 'i'],
    ['h','%', 'x'],
    ['i',' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!'],
]

string = ''
index = 0
for index in range(0, 3):
    for arr in matrix:
        letter = str(arr[index])
        if letter.isalpha() == True:
            string += letter 
            if letter == 's':
                string += ' '
print(string)
