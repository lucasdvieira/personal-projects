from wordList import *
from random import randint

userInput = ''
print('This is a program that generates a bullshit statement.')
userInput = input('Type "yes" for a bullshit phrase otherwise press enter to leave.\n').lower()
while userInput == 'yes':
    aAdverbsIndex = randint(0,len(aAdverbs)-1)
    aAdjectivesIndex = randint(0,len(aAdjectives)-1)
    aVerbsIndex = randint(0, len(aVerbs)-1)
    aNounsIndex = randint(0,len(aNouns)-1)
    print(aAdverbs[aAdverbsIndex],aAdjectives[aAdjectivesIndex],aVerbs[aVerbsIndex],aNouns[aNounsIndex])
    userInput = input('If you\'d like to continue type "yes" otherwise press enter\n').lower()
    




