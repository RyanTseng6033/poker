import random

shapes = ['♤','♡','♢','♧']
cards = ['♧2','♢2','♡2','♤2','♧3','♢3','♡3','♤3','♧4','♢4','♡4','♤4','♧5',
         '♢5','♡5','♤5','♧6','♢6','♡6','♤6','♧7','♢7','♡7','♤7','♧8','♢8',
         '♡8','♤8','♧9','♢9','♡9','♤9','♧10','♢10','♡10','♤10','♧J','♢J','♡J',
         '♤J','♧Q','♢Q','♡Q','♤Q','♧K','♢K','♡K','♤K','♧A','♢A','♡A','♤A']
SIZE = 52
number = [i for i in range (SIZE)]
shuffle = random.sample(number, SIZE)
how_many_players = input('2人玩還是4人玩?')

#如果兩人玩牌
if how_many_players == "2":
    person = [[],[]]
    choice = [[],[]]
    choice_card = [[],[]]
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
#抽牌
    for i in range(1,27):
        for j in range(2):
            choice_card[j] = random.choices(person[j])
            choice[j].append(choice_card[j])
            print(cards[choice_card[j][0]], end = ' ')
            person[j].remove(choice_card[j][0])      
#比大小     
        if choice_card[0] > choice_card[1]:
            print("person 1 win!")
        else:
            print("person 2 win!")
    
#如果四人玩牌
if how_many_players == "4":    
    person = [[],[],[],[]]
    choice = [[],[],[],[]]
    choice_card = [[],[],[],[]]
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
    print("\n")
#抽牌
    for i in range(1,14):
        for j in range(4):
            choice_card[j] = random.choices(person[j])
            choice[j].append(choice_card[j])
            print(cards[choice_card[j][0]], end = ' ')
            person[j].remove(choice_card[j][0])
#比大小    
        if choice_card[0] > choice_card[1] and choice_card[0] > choice_card[2] and choice_card[0] > choice_card[3]:
            print("person 1 win!")
        if choice_card[1] > choice_card[0] and choice_card[1] > choice_card[2] and choice_card[1] > choice_card[3]:
            print("person 2 win!")
        if choice_card[2] > choice_card[1] and choice_card[2] > choice_card[0] and choice_card[2] > choice_card[3]:
            print("person 3 win!")
        if choice_card[3] > choice_card[1] and choice_card[3] > choice_card[2] and choice_card[3] > choice_card[0]:
            print("person 4 win!")
