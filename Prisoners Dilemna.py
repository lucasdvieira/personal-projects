from random import randint

class Player:
    def __init__(self):
        self.isConfessing = False #Shows whether player/computer is confessing
        self.intYearsServing = 0 #Stores how many years player/computer will serve in game

    def computerChooses(self): #Determines whether computer confesses or not
        self.isConfessing = bool(randint(0, 1)) #0 means computer isn't confessing, 1 means computer is confessing

    def playerChooses(self): #Player will indicate whether they will confess or not
        while True:
            try:
                self.playerChoice = input("Press '1' to confess to the crime, press '0' to deny involvement: ")

                if self.playerChoice != "0" and self.playerChoice != "1": #Checks if player typed in one or not; if not, it raises an error
                    raise ValueError("That's not a valid choice")
            except ValueError as exc:
                print(exc)
            else:
                self.isConfessing = bool(int(self.playerChoice)) #stores the players choice as a boolean
                break
        


def assignSentence(isPlayerConfessing, isComputerConfessing): #Takes the choices of player and computer and assigns their sentence accordingly
    
    listSentences = [[(0, 0), (3, 10)], [(10, 3), (6, 6)]] #first number of each tuple years for player, second number of each tuple years for computer

    return listSentences[int(isComputerConfessing)][int(isPlayerConfessing)] #Tuple that's returned depends on computer confession(row), and player confession(column)

def formatOutput(player, computer): #Outputs outcome of game in tabular output
    if player.isConfessing == True: #If True it shows as 'Yes' in output. If not, it shows as 'No' in output
        strPlayerConfessed = "Yes"
    else:
        strPlayerConfessed = "No"

    if computer.isConfessing == True:
        strComputerConfessed = "Yes"
    else:
        strComputerConfessed = "No"

    print("%-15s%-20s%-30s" % ("\nSuspect", "Did they confess?", "How many years are they serving?")) 
    print("%-15s%-20s%-30s" % ("Player", strPlayerConfessed, str(player.intYearsServing) + " years"))
    print("%-15s%-20s%-30s" % ("Computer", strComputerConfessed, str(computer.intYearsServing) + " years\n"))

def storeOutcome(player, computer):
    try: #Checks if the file the outcomes are stored in exists
        storeFile = open("PrisDilemma.txt", "a") #If so, it will append the latest outcome at the bottom of the file
    except FileNotFoundError:
        storeFile = open("PrisDilemma.txt", "w") #If not, it will create a new file to store the outcomes
    finally:
        storeFile.write("Player confessed: " + str(player.isConfessing) + "\n") #These 4 lines is the data being stored
        storeFile.write("Computer confessed: " + str(computer.isConfessing) + "\n")
        storeFile.write("Player is serving: " + str(player.intYearsServing) + " years\n")
        storeFile.write("Computer is serving: " + str(computer.intYearsServing) + " years\n\n")
        storeFile.close()

def displayOutcomes(): #Displays the previoud outcomes from the file they were stored in
    try:
        readFile = open("PrisDilemma.txt", "r") #Checks if the file still exists
    except FileNotFoundError:
        print("Your previous games were not saved properly or were deleted")
    else:
        ctr = 0 
        numOfGames = 1
        for i in readFile:
            if ctr == 0: #Makes sure to output that the next few lines are a new game
                print("\nGame", numOfGames, "\n")
                i = i.strip()
                print(i)
                ctr += 1
            elif ctr < 4: #Outputs the outcomes of game from file
                i = i.strip()
                print(i)
                ctr += 1
            else: #If all the lines of one outcome is printed, ctr made 0 so 'Game [x]' can be outputted
                ctr = 0
                numOfGames += 1
        readFile.close()



player = Player() #initializes player from Player class
computer = Player() #initializes computer from Player class

userInput = ""

while userInput == "": #Main Loop

    player.playerChooses() #Player will choose to confess or not
    computer.computerChooses() #Computer will choose to confess or not

    player.intYearsServing, computer.intYearsServing = assignSentence(player.isConfessing, computer.isConfessing) #Passes player and computer choices, return values is the number of years player and computer will serve

    formatOutput(player, computer)
    storeOutcome(player, computer)

    seeOutcome = input("Press a key and enter to see outcomes of previous games. Press enter to continue: ")

    if seeOutcome != "": #Checks if user wants to see the outcomes of the previous games
        displayOutcomes()

    userInput = input("\nPress enter to continue, press a key and enter to quit: ") 


