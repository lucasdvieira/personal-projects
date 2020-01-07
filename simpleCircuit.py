# import randint
from random import randint

#andGate
def andGate(a,b):
    if a == 1 and b == 1:
        return True
        
    else:
        return False

#orGate
def orGate(a,b):
    if a == 1 or b == 1:
        return True
    else:
        return False

#norGate
def norGate(a,b):
    c = b
    if a == 1 or c == 1:
        return False
    else:
        return True

# Initialize randint and run checks on logic gates.
while True:
    userInput = input("Press enter to run logic or any other key to exit: ")
    a = randint(0,1)
    b = randint(0,1)
    c = randint(0,1)
    print(f'A: {a}')
    print(f'B: {b}')
    print(f'C: {c}')
    # Or Gate
    if norGate(a,b) or andGate(b,c):
        print('True')
    else:
        print('False')
    if userInput != '':
        break
    
    
    





