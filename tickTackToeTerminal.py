RED = '\033[93m'
GREEN = '\033[92m'
ENDC = '\033[0m'


def displayGrid(xFields, oFields, greenFields=[], redFields=[]):
    contents = ["X" if x in xFields else "O" if x in oFields else " " for x in range(0, 9)]

    if greenFields:
        contents = [GREEN + val + ENDC if i in greenFields else val for i, val in enumerate(contents)]

    if redFields:
        contents = [RED + val + ENDC if i in redFields else val for i, val in enumerate(contents)]

    print(f" {contents[0]} | {contents[1]} | {contents[2]} ")
    print(" --+---+-- ")
    print(f" {contents[3]} | {contents[4]} | {contents[5]} ")
    print(" --+---+-- ")
    print(f" {contents[6]} | {contents[7]} | {contents[8]} ")


def displayCustomGrid(fields, greenFields=[], redFields=[]):
    contents = [([score for field, score in fields if x == field] or (" "))[0] for x in range(0, 9)]

    if greenFields:
        contents = [GREEN + val + ENDC if i in greenFields else val for i, val in enumerate(contents)]

    if redFields:
        contents = [RED + val + ENDC if i in redFields else val for i, val in enumerate(contents)]

    print(f"{str(contents[0]).rjust(2, ' ')} |{str(contents[1]).rjust(2, ' ')} |{str(contents[2]).rjust(2, ' ')} ")
    print(" --+---+-- ")
    print(f"{str(contents[3]).rjust(2, ' ')} |{str(contents[4]).rjust(2, ' ')} |{str(contents[5]).rjust(2, ' ')} ")
    print(" --+---+-- ")
    print(f"{str(contents[6]).rjust(2, ' ')} |{str(contents[7]).rjust(2, ' ')} |{str(contents[8]).rjust(2, ' ')} ")


def getInput(text, acceptedValues, displayOptions=True):
    if not acceptedValues:
        raise Exception("no acceptedValues given")

    while True:
        userInput = input("\n" + text + (f"\nFolgende eingaben sind verfügbar: {', '.join(str(e) for e in acceptedValues)}\n" if displayOptions else "\n"))

        if userInput in [str(e) for e in acceptedValues]:
            return userInput

        print("invalide Eingabe")


# displayGrid([0, 1, 2], [5, 8], [0, 1, 2])
# getInput("Welches Feld?", ["3", "4", "6", "7"])
