# 1. Choose a random word
# 2. Display Letters using "-"
# 3. user have to guess the letter
# 4. if guess is correct replace the "-" with letter on display
# 5. if guess is wrong deduct a live

from ntpath import join
import random

words = ["ambuj", "kumar", "dubey"]

usedLetters = set()

live = 5


def choosingRandomWord(words):
    global randomWord
    randomWord = random.choice(words)

    displayWord(randomWord)


def displayWord(randomWord):
    word = [letter if letter in usedLetters else "-" for letter in randomWord]

    if "-" in word and live != 0:
        print("Word is ", " ".join(word))
        print("Letters used: ", " ".join(usedLetters))
        userGuess()
    elif live == 0:
        print("Your live ended")
    else:
        print("You have succesfully guessed the word ", "".join(word))


def userGuess():
    letterGuessed = input("Guess the letter: ")

    compare(letterGuessed)


def compare(letterGuessed):
    global usedLetters
    global live

    if letterGuessed not in usedLetters:
        usedLetters.add(letterGuessed)

        if letterGuessed not in set(randomWord):
            live -= 1

        displayWord(randomWord)

    else:
        print("You cannot use same letter again")

        userGuess()


choosingRandomWord(words)
