from ttthelper import clear, getWinner, getEmptyFields # type: ignore
import copy
import random

from tickTackToeTerminal import displayGrid, getInput, displayCustomGrid # type: ignore

def swapFields(playerFields):
    return [playerFields[1], playerFields[0]]


def addFieldToCopy(playerFields, newField, index=0):
    copied = copy.deepcopy(playerFields)
    copied[index].append(newField)
    return copied


iters = 10000
def getOptions(playerFields, playerIndex):
    fields = getEmptyFields(playerFields[0], playerFields[1])

    reses = [(field, sum([mcts(addFieldToCopy(playerFields, field, 1), False) for _ in range(iters)])) for field in fields]
    print(reses)

    return (max(reses, key=lambda x: x[1])[0], reses)


def mcts(playerFields, curPlayerShouldWin):

    winner, _ = getWinner(playerFields[0], playerFields[1])

    # Tie
    if winner == 2:
        return 0

    # Player at first Pos won
    if winner == 0:
        return 1 if curPlayerShouldWin else -1

    # Player at second Pos won
    if winner == 1:
        return -1 if curPlayerShouldWin else 1

    # no player won yet and no draw
    field = random.choice(getEmptyFields(playerFields[0], playerFields[1]))
    return mcts(swapFields(addFieldToCopy(playerFields, field)), not curPlayerShouldWin)


playVictoryText = ["Player X Won!", "Player O Won!"]
aiVictoryText = "The AI Won!"


def playGame():
    clear()

    playerFields = [
        [],
        []
    ]

    currentPlayerIsX = not True
    # aiPlayer = random.randint(0, 1) == 0
    aiPlayerIsX = True

    # gameVsAi = getInput("who do you want to play against?", ["player", "ai"]) == "ai"
    gameVsAi = True
    clear()

    while True:
        currentPlayerIsX = not currentPlayerIsX

        print("")
        displayGrid(playerFields[0], playerFields[1], redFields=playerFields[+currentPlayerIsX][-1:])

        if gameVsAi and currentPlayerIsX == aiPlayerIsX:
            maxField, fields = getOptions(playerFields, currentPlayerIsX)

            print()
            print(playerFields)
            displayCustomGrid(fields)
            print(maxField + 1)

            userInput = maxField
            input()

        else:
            userInput = int(getInput(f"wo möchtest du dein {'x' if currentPlayerIsX else 'o'} setzen?", [x + 1 for x in getEmptyFields(playerFields[0], playerFields[1])])) - 1

        playerFields[+currentPlayerIsX].append(int(userInput))

        winner, fields = getWinner(playerFields[0], playerFields[1])

        clear()

        if winner == -1: continue

        print("")
        displayGrid(playerFields[0], playerFields[1], greenFields=fields)

        if winner == 2: print("\nDraw\n")
        else: print(aiVictoryText if gameVsAi else playVictoryText[+currentPlayerIsX])

        break

    if getInput("GG! Do you want to play again?", ["yes", "no"], displayOptions=False) == "yes":
        playGame()



if __name__ == "__main__":
    playGame()
