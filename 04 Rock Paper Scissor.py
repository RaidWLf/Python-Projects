# 1. computer needs to select between rock paper or scissor
# 2. user needs to enter his own selection
# 3. compare both and generate and store result
# 4. repeat untill user quits and then print the result

import random

# creating the game stack
game = ["r", "p", "s"]

win = 0
loss = 0
tie = 0


def computer():
    # computer choice
    computerChoice = random.choice(game)

    user(computerChoice)


def user(computerChoice):
    userChoice = input(
        "Enter your choice Rock (R), Paper (P) and Scissor (S) and for Quit (Q) :  ")

    compare(computerChoice, userChoice)


def tied():
    global tie
    tie += 1
    print("Game tied")


def wined():
    global win
    win += 1
    print("You won")


def lossed():
    global loss
    loss += 1
    print("You loss")


def compare(computerChoice, userChoice):
    if (userChoice == "r"):
        if (computerChoice == "r"):
            tied()
        elif (computerChoice == "s"):
            wined()
        else:
            lossed()

        computer()

    elif (userChoice == "p"):
        if (computerChoice == "s"):
            lossed()
        elif (computerChoice == "p"):
            tied()
        else:
            wined()

        computer()

    elif (userChoice == "s"):
        if (computerChoice == "s"):
            tied()
        elif (computerChoice == "p"):
            wined()
        else:
            lossed()

        computer()

    elif (userChoice == "q"):
        quitGame()

    else:
        print("Wrong choice")

        user(computerChoice)


def quitGame():
    global win
    global loss
    global tie
    print("Thanks for playing the game")
    print(f"Results are win: {win}, loss: {loss} and tie: {tie}")


computer()
