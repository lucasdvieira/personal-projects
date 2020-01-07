import random
aCardNames = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
aCardValues = [2, 3, 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 ]
aSuits = ["♠","♥","♦","♣"]
aCards = [[""for i in range(52)] for j in range(3)]
#Initializing counters
c = 0
s = 0
i = 0
#Initalizing each hand
Hand1 = [[],[],[]]
Hand2 = [[],[],[]]
Hand3 = [[],[],[]]
#Function checks and returns the total card value of each hand.
def handvalue(hand):
    return sum(hand[2])
#Function addCards checks if coniditon requires to add another card.
def addcards(Hand):
    Hand[0].append(aCards[0].pop(0))
    Hand[1].append(aCards[1].pop(0))
    Hand[2].append(aCards[2].pop(0))
    i = 0
    while i < len(Hand[2]):
        print(Hand[0][i],Hand[1][i],Hand[2][i])
        i += 1
    print("The value:", handvalue(Hand))
#Creating the Deck of Cards
while s < 4:
    while c < 13:
        aCards[0][i] = aCardNames[c]
        aCards[1][i] = aSuits[s] 
        aCards[2][i] = aCardValues[c]
        c += 1
        i += 1
    s += 1
    c = 0
#Shuffle Deck
for b in range(0,51):
    c = random.randint(0,51)
    Temp = aCards[0][c]
    aCards[0][c] = aCards[0][b]
    aCards[0][b] = Temp
    Temp = aCards[1][c]
    aCards[1][c] = aCards[1][b]
    aCards[1][b] = Temp
    Temp = aCards[2][c]
    aCards[2][c] = aCards[2][b]
    aCards[2][b] = Temp
#Assign cards to each hand

for i in range (2):
    Hand1[0].append(aCards[0].pop(0))
    Hand1[1].append(aCards[1].pop(0))
    Hand1[2].append(aCards[2].pop(0))
    Hand2[0].append(aCards[0].pop(0))
    Hand2[1].append(aCards[1].pop(0))
    Hand2[2].append(aCards[2].pop(0))
    Hand3[0].append(aCards[0].pop(0))
    Hand3[1].append(aCards[1].pop(0))
    Hand3[2].append(aCards[2].pop(0))
#Print Player 1 hand
print("----------------------------Player 1 hand-------------------------------------")
i = 0
while i < 2:
    print(Hand1[0][i],Hand1[1][i],Hand1[2][i])
    i += 1
print("The value:", handvalue(Hand1))
print()
#Print Player 2 hand
print("----------------------------Player 2 hand-------------------------------------")
i = 0
while i < 2:
    print(Hand2[0][i],Hand2[1][i],Hand2[2][i])
    i += 1
print("The value:", handvalue(Hand2))
#Print Player 3 hand
i = 0
print("----------------------------Player 3 hand-------------------------------------")
while i < 2:
    print(Hand3[0][i],Hand3[1][i],Hand3[2][i])
    i += 1
print("The value:", handvalue(Hand3))
#If card(s) added, print Player 1 Hand
while handvalue(Hand1) < 17:
    print("----------------------------Player 1 hand-------------------------------------")
    addcards(Hand1)
#If card(s) added, print Player 2 Hand
while handvalue (Hand2) < 17:
    print("----------------------------Player 2 hand-------------------------------------")
    addcards(Hand2)
#If card(s) added, print Player 3 Hand
while handvalue (Hand3) < 17:
    print("----------------------------Player 3 hand-------------------------------------")
    addcards(Hand3)
