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
    choice = [[],[]]
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
  #1        
    for i in range(1,27):
        choice_card = random.choices(person[0])
        choice[0].append(choice_card)
        print(cards[choice_card[0]], end = ' ')
        person[0].remove(choice_card[0])
    print("\n")
  #2
    for i in range(1,27):
        choice_card_2 = random.choices(person[1])
        choice[1].append(choice_card_2)
        print(cards[choice_card_2[0]], end = ' ')
        person[1].remove(choice_card_2[0])
    
#如果四人玩牌
if how_many_players == "4":    
    person = [[],[],[],[]]
    choice = [[],[],[],[]]
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
  #1        
    for i in range(1,14):
        choice_card = random.choices(person[0])
        choice[0].append(choice_card)
        print(cards[choice_card[0]],end = ' ')
        person[0].remove(choice_card[0])
    print("\n")    
  #2
    for i in range(1,14):
        choice_card_2 = random.choices(person[1])
        choice[1].append(choice_card_2)
        print(cards[choice_card_2[0]],end = ' ')
        person[1].remove(choice_card_2[0])
    print("\n")
  #3
    for i in range(1,14):
        choice_card_3 = random.choices(person[2])
        choice[1].append(choice_card_3)
        print(cards[choice_card_3[0]],end = ' ')
        person[2].remove(choice_card_3[0])
    print("\n")
  #4
    for i in range(1,14):
        choice_card_4 = random.choices(person[3])
        choice[1].append(choice_card_4)
        print(cards[choice_card_4[0]],end = ' ')
        person[3].remove(choice_card_4[0])
