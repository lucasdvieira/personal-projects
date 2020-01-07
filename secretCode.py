#import random and string
import random
import string

#Initialize and shuffle array
randArray = [i for i in range(26)]
random.shuffle(randArray)

#Initialize array of lowercase letters
letterArray = list(string.ascii_lowercase)

# Iterates through ever letter and assigns newIndex, and prints new and old index.
# Concatenates individual letters to form encrypted word. 
while True:
    userWord = input("enter string to encrypt: ")
    encryptedWord = ''
    if userWord != '':
        for letter in userWord:
            letterIndex = letterArray.index(letter)
            randomIndex = randArray[letterIndex]
            encryptedLetter = letterArray[randomIndex]
            encryptedWord += encryptedLetter
            print(letter,letterIndex,randomIndex)
        print(encryptedWord)
    else:
        break
            
