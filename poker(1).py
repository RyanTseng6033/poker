import random

person_one = []
person_two = []

shapes = ['♡','♧','♤','♢']

cards = ['♤A','♤2','♤3','♤4','♤5','♤6','♤7','♤8','♤9','♤10','♤J','♤Q','♤K',
         '♡A','♡2','♡3','♡4','♡5','♡6','♡7','♡8','♡9','♡10','♡J','♡Q','♡K',
         '♢A','♢2','♢3','♢4','♢5','♢6','♢7','♢8','♢9','♢10','♢J','♢Q','♢K',
         '♧A','♧2','♧3','♧4','♧5','♧6','♧7','♧8','♧9','♧10','♧J','♧Q','♧K']

SIZE = 52
number = [i for i in range (SIZE)]

shuffle = random.sample(number, SIZE)

for i in range (SIZE):    
    index = shuffle [i-1]
    if i % 2 == 0:
        person_one.append(cards[index])
    if i % 2 != 0:
        person_two.append(cards[index])
print(person_one)
print('\n')
print(person_two)
   

