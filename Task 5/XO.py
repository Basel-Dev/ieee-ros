import subprocess
import platform

# Winning conditions: One row / col / diagonal have the same symbol
# gameList is a 2D List, 3 Rows, 3 Columns => XO board

def getColumn(gameList, index):
    return [gameList[x][index] for x in range(3)]


def getDiagonals(gameList):
    return [
        [gameList[x][x] for x in range(3)],  ## (0, 0), (1, 1), (2, 2)
        [gameList[x][2 - x] for x in range(3)],  ## (0, 2), (1, 1), (2, 0)
    ]


def checkWinningConditions(gameList, validPositions):
    winner = None

    # Row / Col / Diagonal check for winner
    for i in range(3):
        row = gameList[i]
        col = getColumn(gameList, i)

        if len(set(row)) == 1:
            winner = row[0]
            break

        if len(set(col)) == 1:
            winner = col[0]
            break

    if not winner:
        for diagonal in getDiagonals(gameList):
            if len(set(diagonal)) == 1:
                winner = diagonal[0]

    # If there's a winner, game is complete regardless of numbers
    # if no more validPositions and no winner => Draw
    # if not these cases => game is incomplete, continue to next turn

    if winner:
        return {"draw": False, "gameComplete": True}
    elif len(validPositions) > 0:
        return {"gameComplete": False}
    else:
        return {"draw": True, "gameComplete": True}


def displayGame(gameList):
    ## Clear terminal
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

    ## Print the current gameList board
    for i in range(3):
        displayRow = " | ".join(gameList[i])  ## 1 | 2 | 3
        print(displayRow)

        if i != 2:
            print("—————————")
        else:
            print()


## Choosing custom symbols

symbolDict = {"X": "X", "O": "O"}

for symbol in symbolDict.keys():
    position = "first" if symbol == "X" else "second"

    ## Input Validity loop, break out of the loop once valid
    while True:
        inputtedSymbol = input(f"Input {position} player's symbol (default: {symbol}): ")

        if inputtedSymbol.isalpha() and len(inputtedSymbol) == 1:
            symbolDict[symbol] = inputtedSymbol
        elif inputtedSymbol == "":
            pass
        else:
            print("Invalid Symbol, Must be one character and cannot be a number")
            continue
        break


## Get valid position, while loop => break when valid
def getPositionInput(turn, validPositions):
    while True:
        positionInput = input(f"Input {symbolDict[turn]}'s Position: ")
        if positionInput in validPositions:
            validPositions.remove(positionInput)
            break
        else:
            print("Invalid Position")
            continue

    return positionInput


## Replace a position on the gameList with symbol depending on the turn
def replacePosWithSymbol(gameList, posInput, turn):
    for x in range(3):
        for y in range(3):
            if gameList[x][y] == posInput:
                gameList[x][y] = symbolDict[turn]


scoreDict = {"X": 0, "O": 0}
# playRound => Start game cycle, recursively call back for another round
# Turns are represented with X and O in the code but are printed to the user with their custom symbol
def playRound():
    currentGameList = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]

    validPositions = list("123456789")

    # Cycle: Begin with X => Get Position and Place Symbol
    # => Check Winning Conditions => end if winner/draw else switch turns & repeat

    turn = "X"
    while True:
        displayGame(currentGameList)

        positionInput = getPositionInput(turn, validPositions)
        replacePosWithSymbol(currentGameList, positionInput, turn)

        conditions = checkWinningConditions(currentGameList, validPositions)

        if not conditions["gameComplete"]:
            turn = "O" if turn == "X" else "X"
            continue
        else:
            displayGame(currentGameList)
            
            if conditions["draw"]:
                print("It's a draw!")
            else:
                scoreDict[turn] += 1
                print(f"{symbolDict[turn]} won!")
        break

    print(f"\nCurrent points are {scoreDict['X']}-{scoreDict['O']}")


while True:
    playRound()

    continuePlaying = input("Want to play another round? (Y/N): ")
    if continuePlaying.lower() == "y":
        continue
    else:
        print(f"Final points are {scoreDict['X']}-{scoreDict['O']}")
        break
