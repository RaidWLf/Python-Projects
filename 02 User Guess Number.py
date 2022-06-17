# 1. Computer needs to generate a random number between a range
# 2. User have to guess the number
# 3. Computer needs to provide feedback to user on thier guess
# 4. Print the Number if guess is correct
# 5. Rerun step 2 and 3 if guess is incorrect

import random

# generating random number


def generateRandom(highRange):
    global randomNumber
    randomNumber = random.randint(1, highRange)

    userInput()


# user input
def userInput():
    guessedNumber = int(input(f"Guess the number between 1 and {highRange}: "))

    computerFeedback(guessedNumber)

# computer's feedback


def computerFeedback(guessedNumber):
    if (guessedNumber == randomNumber):
        print(f"Yay You guessed the number {randomNumber}")

    elif (guessedNumber > randomNumber):
        print(f"Your guess is too high")
        userInput()

    else:
        print(f"Your guess is too low")
        userInput()


highRange = int(input("Enter the highest range for the game: "))

generateRandom(highRange)
