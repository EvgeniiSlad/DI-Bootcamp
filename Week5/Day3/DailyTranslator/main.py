# pip3 install translate
# pip3 install googletrans
from translate import Translator
translate=Translator(from_lang='FR',to_lang='RUS')
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
dict1 = {}

for word in french_words:
    dict1[translate.translate(word)]=word

print(dict1)
