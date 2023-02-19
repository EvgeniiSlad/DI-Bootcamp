from random import randint, sample


fileloc='/Users/evgeniisladkov/Desktop/DI-Bootcamp/Week5/Day4/ExercisesXP/text.txt'
print(fileloc)
def get_words_from_file(file):
    with open(file,'r') as f:
        words_list=[]
        for word in f:
            words_list += word.split()
        return words_list
# print(get_words_from_file(fileloc))
def get_random_sentence(length):
    word_list = get_words_from_file(fileloc)
    sentence = ''
    str_length = 0
    while str_length < length:
        random_index = word_list[randint(0, len(word_list)-1)]
        sentence += ' ' + random_index
        str_length += 1
    return sentence

 
get_random_sentence(4)


def main():
    print('This program takes the random words and create a sentence, the sentence should be lower case')
    sentence_length = int(input('Sentence length: '))
    if 2 < sentence_length < 20:
        random_sentence = str(get_random_sentence(sentence_length))
        print(random_sentence.lower())

main()


