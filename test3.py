import random

deck = []
nums = []
shapes = '♥♣♠◆'
player_total = 0
dealer_total = 0
def check(Cards,nums):
    total1 = 0
    total2 = 0
    for i in range(nums):
        J = Q = K = ACE_1 = ACE_11 = num = 0
        if(Cards[i][1] == "J"): J = 10
        elif(Cards[i][1] == "Q"): Q = 10
        elif(Cards[i][1] == "K"): K = 10
        elif(Cards[i][1] == "A"): ACE_1 = 1
        elif(Cards[i][1] == "A"): ACE_11 = 11
        else: num = int(Cards[i][1])
        total1 = total1 + num + J + Q + K + ACE_1 
        total2 = total2 + num + J + Q + K + ACE_11
    if(abs(total1 - 21) < abs(total2 - 21)) : return total1
    else : return total2

def check_over(nums):
    if(nums > 21): return True
    else : return False

def win_or_lose(num1,num2):
    if(num1 > num2) : return True
    elif(num1 == num2) : print("DRAW")
    else : return False

for i in range(1,14):
    if i == 1:
        nums.append("A")
    elif i == 11:
        nums.append("J")
    elif i == 12:
        nums.append("Q")
    elif i == 13:
        nums.append("K")
    else:
        nums.append(str(i))

for shape in shapes:
    for num in nums:
        deck.append((shape, num))

random.shuffle(deck)
initial_deck = deck
while True :
    player = []
    dealer = []        
    for i in range(2):
        dealer.append(deck.pop())
        player.append(deck.pop())
    while True:
        dealer_total = check(dealer,len(dealer))

        print("dealer","     ?     ",end = ' ')
        for i in range(1, len(dealer)):
            print(dealer[i],end = ' ')

        print("\nplayer",end = ' ')

        for i in range(len(player)):
            print(player[i],end = ' ')

        if(check_over(dealer_total) == True):
            print("dealer lose")
            break

        select = input("\nhit or stand or exit : ")
        if(select == "hit"):
            print("\n\n")
            player.append(deck.pop())
            player_total = check(player,len(player))
            if(check_over(player_total) == True):
                print("player lose")
                break
        elif(select == "stand"):
            player_total = check(player,len(player))
            if(win_or_lose(dealer_total,player_total)):
                print("player lose")
                break
            else:
                print("player win")
                break
        elif(select == "exit"):
            break
        else:
            print("Wrong command")
        
        if(dealer_total < 17):
            dealer.append(deck.pop())
            dealer_total = check(dealer,len(dealer))
        
        if(check_over(dealer_total) == True):
            print("player win")
            break 

        if(check_over(dealer_total) == True):
            print("dealer lose")
            break

    print("dealer",end = ' ')
    for i in range(len(dealer)):
        print(dealer[i],end = ' ')

    print("\nplayer",end = ' ')

    for i in range(len(player)):
        print(player[i],end = ' ')
    
    print("\n\n\n")
    if(len(deck) < 8) : deck = initial_deck
    
        