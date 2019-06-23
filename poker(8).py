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
    for i in range(1):
        person[i].sort()
        for index in person[i]:
            print(cards[index], end = '\t')   
        print("\n")
    for entry in person[0]:
        print(entry, end = '\t')
    print("\n")    
#抽牌
    for i in range(1,27):
        choice_card[0] = int(input("你要選哪一張牌?"))
        print("\n")
        choice[0].append(choice_card[0])
        print("你的牌:",cards[choice_card[0]],end = '     ')
        person[0].remove(choice_card[0])
        
        choice_card[1] = random.choices(person[1])
        choice[1].append(choice_card[1])
        print("電腦:",cards[choice_card[1][0]])
        person[1].remove(choice_card[1][0])
        print("\n")
#比大小     
        if choice_card[0] > int(str(choice_card[1][0])):
            print("你贏了!")
            print("----------------------------------------------------------------------------------------------")
        else:
            print("電腦贏了")
            print("----------------------------------------------------------------------------------------------")

        for index in person[0]:
            print(cards[index], end = '\t')
        print("\n")    
        for entry in person[0]:
            print(entry, end = '\t')
        print("\n")
    
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
    for i in range(3):
        person[i].sort()
        
    person[3].sort()
    for index in person[3]:
        print(cards[index], end = '\t')   
    print("\n")
    for entry in person[3]:
        print(entry, end = '\t')
    print("\n")
#抽牌
    for i in range(1,14):
        choice_card[3] = int(input("你要選哪一張牌?"))
        print("\n")
        choice[3].append(choice_card[3])
        person[3].remove(choice_card[3])
        
        for j in range(3):
            choice_card[j] = random.choices(person[j])
            choice[j].append(choice_card[j])
            print("電腦",j+1,":",cards[choice_card[j][0]], end = '     ',)
            person[j].remove(choice_card[j][0])
        print("你的牌:",cards[choice_card[3]])
        print("\n")

#比大小    
        if int(str(choice_card[0][0])) > int(str(choice_card[1][0])) and int(str(choice_card[0][0])) > int(str(choice_card[2][0])) and int(str(choice_card[0][0])) > int(str(choice_card[3])):
            print("電腦1贏了!")
            print("----------------------------------------------------------------------------------------------")
        if int(str(choice_card[1][0])) > int(str(choice_card[0][0])) and int(str(choice_card[1][0])) > int(str(choice_card[2][0])) and int(str(choice_card[1][0])) > int(str(choice_card[3])):
            print("電腦2贏了!")
            print("----------------------------------------------------------------------------------------------")
        if int(str(choice_card[2][0])) > int(str(choice_card[1][0])) and int(str(choice_card[2][0])) > int(str(choice_card[0][0])) and int(str(choice_card[2][0])) > int(str(choice_card[3])):
            print("電腦3贏了!")
            print("----------------------------------------------------------------------------------------------")
        if int(str(choice_card[3])) > int(str(choice_card[1][0])) and int(str(choice_card[3])) > int(str(choice_card[2][0])) and int(str(choice_card[3])) > int(str(choice_card[0][0])):
            print("你贏了!")
            print("----------------------------------------------------------------------------------------------")

        for index in person[3]:
            print(cards[index], end = '\t')
        print("\n")    
        for entry in person[3]:
            print(entry, end = '\t')
        print("\n")            
