#1
# users_word = input('enter a word: ')
# dictn = {}
# for i, letter in enumerate(users_word):
#     if letter not in dictn:
#      dictn[letter] = []
#      dictn[letter].append(i)
#     elif letter in dictn:
#          dictn[letter].append(i)
# print(dictn)

#2
items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

money_in_wallet = int(input('How much money do you have in your wallet: '))
can_afford = []      
cant_afford = []
for key, price in items_purchase.items():
    money = price.replace(price[0], '')
    if ',' in money:
        money = money.split(',')
        money = ''.join(money)
    if int(money) <= money_in_wallet:
        can_afford.append(key)
    else:
        cant_afford.append(price)

if len(cant_afford) == len(items_purchase):
    print('nothing')
else:
    print(sorted(can_afford))
