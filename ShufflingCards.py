#Initializes a standard deck of cards

from random import *

cardNames = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #All available card names
cardValues = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"] #All available card values
cardSuits = ["Spades", "Clovers", "Diamonds", "Hearts"] #All available card suits

stdDeck = [["" for i in range(3)] for j in range(52)] #Declares empty standard deck

ctr = 0

for k in range(13): #Loop initializes a standard deck of cards in proper order
    for l in range(4):
        stdDeck[ctr][0] = cardNames[k]
        stdDeck[ctr][1] = cardSuits[l]
        stdDeck[ctr][2] = cardValues[k]
        
        ctr += 1

isQuitting = ""

while isQuitting == "":

    #Shuffling Deck
    
    ctr = 0
    
    tempList = ["" for i in range(52)] 
    
    newDeck = stdDeck #newDeck will be shuffled, while stdDeck is a reference deck

    for k in range(len(stdDeck)): #for loop shuffles deck using tempList
        x = randint(0, 51)

        tempList[k] = newDeck[k]
        newDeck[k] = newDeck[x]
        newDeck[x] = tempList[k]

    #Assign Poker Hands

    pokerHand1 = [["" for i in range(3)] for j in range(5)] 
    pokerHand2 = [["" for i in range(3)] for j in range(5)]

    for i in range(5):
        pokerHand1[i][0] = newDeck[i][0] #Assigns first five cards in newDeck to 1st Poker Hand
        pokerHand1[i][1] = newDeck[i][1]
        pokerHand1[i][2] = newDeck[i][2]

        pokerHand2[i][0] = newDeck[i + 5][0] #Assigns next five cards in newDeck to 1st Poker Hand
        pokerHand2[i][1] = newDeck[i + 5][1]
        pokerHand2[i][2] = newDeck[i + 5][2]

    #Outputs Poker Hands
        
    print("\n\n1st Poker Hand")

    print("Card Number\tSuit\t\tValue")

    for i in range(len(pokerHand1)):
        print("%-16s%-16s%-16s" % (pokerHand1[i][0], pokerHand1[i][1], pokerHand1[i][2])) #outputs 1st poker hand's cards (as well as their suits and values)

    print("\n\n2nd Poker Hand")

    print("Card Number\tSuit\t\tValue")

    for i in range(len(pokerHand2)):
        print("%-16s%-16s%-16s" % (pokerHand2[i][0], pokerHand2[i][1], pokerHand2[i][2])) #outputs 2nd poker hand's cards (as well as their suits and values)

    isQuitting = input("\nPress Enter to rerun program. Press any other key and Enter to quit: ") #Used to rerun main loop or quit
