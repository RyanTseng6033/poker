import random

shapes = ['♤','♡','♢','♧']
cards = ['♤A','♤2','♤3','♤4','♤5','♤6','♤7','♤8','♤9','♤10','♤J','♤Q','♤K',
         '♡A','♡2','♡3','♡4','♡5','♡6','♡7','♡8','♡9','♡10','♡J','♡Q','♡K',
         '♢A','♢2','♢3','♢4','♢5','♢6','♢7','♢8','♢9','♢10','♢J','♢Q','♢K',
         '♧A','♧2','♧3','♧4','♧5','♧6','♧7','♧8','♧9','♧10','♧J','♧Q','♧K']

SIZE = 52
number = [i for i in range (SIZE)]
shuffle = random.sample(number, SIZE)
how_many_players = input('2人玩還是4人玩?')

#如果兩人玩牌
if how_many_players == "2":
    person = [[],[]]
#洗牌
    for i in range (SIZE):    
        index = shuffle [i-1]
        if i % 2 == 0:
            person[0].append(index)       
        if i % 2 == 1:
            person[1].append(index)

#發牌
    for i in range(2):
        person[i].sort()
        print('person',i+1,':')
        for index in person[i]:
            print(cards[index], end = ' ')
        print("\n")

#如果四人玩牌
if how_many_players == "4":    
    person = [[],[],[],[]]
#洗牌
    for i in range (SIZE):    
        index = shuffle [i-1]
        if i % 4 == 0:
            person[0].append(index)       
        if i % 4 == 1:
            person[1].append(index)
        if i % 4 == 2:
            person[2].append(index)
        if i % 4 == 3:
            person[3].append(index)

#發牌
    for i in range(4):
        person[i].sort()
        print('person',i+1,':')
        for index in person[i]:
            print(cards[index], end = ' ')
        print("\n")
