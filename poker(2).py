import random

person_one = []
person_two = []
person_three = []
person_four = []
shapes = ['♤','♡','♢','♧']
cards = ['♤A','♤2','♤3','♤4','♤5','♤6','♤7','♤8','♤9','♤10','♤J','♤Q','♤K',
         '♡A','♡2','♡3','♡4','♡5','♡6','♡7','♡8','♡9','♡10','♡J','♡Q','♡K',
         '♢A','♢2','♢3','♢4','♢5','♢6','♢7','♢8','♢9','♢10','♢J','♢Q','♢K',
         '♧A','♧2','♧3','♧4','♧5','♧6','♧7','♧8','♧9','♧10','♧J','♧Q','♧K']

SIZE = 52
number = [i for i in range (SIZE)]
shuffle = random.sample(number, SIZE)

for i in range (SIZE):    
    index = shuffle [i-1]
    if i % 4 == 0:
        person_one.append(index)       
    if i % 4 == 1:
        person_two.append(index)
    if i % 4 == 2:
        person_three.append(index)
    if i % 4 == 3:
        person_four.append(index)
person_one.sort()
print('person one:')
for index in person_one:
    print(cards[index], end = ' ')
print("\n")
person_two.sort()
print('person two:')
for index in person_two:
    print(cards[index], end = ' ')
print("\n")
person_three.sort()
print('person three:')
for index in person_three:
    print(cards[index], end = ' ')
print("\n")
person_four.sort()
print('person four:')
for index in person_four:
    print(cards[index], end = ' ')
