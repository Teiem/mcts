import os


def clear():
    os.system('cls')

# 2 := draw
# 0, 1 player numbers
# -1 no winner
def getWinner(xPlayerFields, oPlayerFields):
    if len(xPlayerFields) + len(oPlayerFields) == 9:
        return (2, [])

    winningConfigs = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6],
    ]

    for player, playerFields in enumerate([xPlayerFields, oPlayerFields]):
        for fields in winningConfigs:
            if all([field in playerFields for field in fields]):
                return (player, fields)

    return (-1, [])


def getEmptyFields(xPlayerFields, oPlayerFields):
    return [x for x in range(0, 9) if x not in xPlayerFields + oPlayerFields]