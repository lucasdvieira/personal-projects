import random
userInput = 'yes'
while userInput == 'yes':
    randomNumber = []

    while len(randomNumber) < 5:
        randomNum = random.randint(1,38)
        while randomNum in randomNumber:
            randomNum = random.randint(1,38)
        randomNumber.append(randomNum)
    print('These are the cash 5 numbers')
    for num in randomNumber:
        print(num, end=' ')
    print()
    userInput = input('Would you like to play again?  Type "yes" to play or "no": ')

    
