# 1. Computer needs to guess the number
# 2. User needs to provide feedback
# 3. if guess is correct Print the guess
# 4. if guess is not true Set Low and High according to feedback
# 5. Repeat step 1 to 3 untill guess is true


import random


def computerGuess(low, high):
    # Computer guess
    print(f"Guessing Number between {low} and {high}")
    global guessedNumber
    guessedNumber = random.randint(low, high)

    userFeedback()


def userFeedback():
    # user feedback
    feedback = input(
        f"Is the {guessedNumber} correct (C), high (H), or low (L): ").lower()

    compareFeedback(feedback)


def compareFeedback(feedback):
    # Comparing the feedback
    global low
    global high
    if (feedback == "c"):
        print(f"Yay Computer guessed the number {guessedNumber} correctly")

    elif (feedback == "h"):
        high = guessedNumber - 1
        computerGuess(low, high)

    elif (feedback == "l"):
        low = guessedNumber + 1
        computerGuess(low, high)

    else:
        print("Print enter the correct input")
        userFeedback()


low = 1
high = int(input("Enter the highest range for game: "))

computerGuess(low, high)
