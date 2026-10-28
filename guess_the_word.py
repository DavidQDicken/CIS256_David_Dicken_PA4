# David Dicken
# CIS256 Fall 2026
# Programming Assignment 4

"""
This is a word guessing game. You have to guess the correct word one letter
at a time. Once you have made three wrong guesses you are out.
"""


import random


words = ["music", "school", "garage", "sky", "banana"]


def display_word_status(selected_word, guessed_letters):
    """Shows which letters in the word you have guessed and hides the rest"""
    word_status = ""
    for letter in selected_word:
        if letter not in guessed_letters:
            word_status += "_"
        else:
            word_status += letter
    return word_status


def check_guess(strikes, guess, selected_word, guessed_letters):
    """Checks for incorrect input and counts up wrong guesses."""
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
    else:
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess not in  selected_word:
                print("Wrong guess!")
                strikes = strikes + 1
            else:
                print("Correct guess!")
        else:
            print("You have already guessed this letter.")
    return strikes


def start_game():
    """
    Prompts the user to guess a letter untill the word is either
    correctly guessed or three strikes are reached.
    """
    selected_word = random.choice(words)
    guessed_letters = []
    strikes = 0

    print("Guess the word using one letter at a time.")

    while strikes < 3:
        print()
        print(display_word_status(selected_word, guessed_letters))
        print("Letters guessed:", guessed_letters)
        print("strikes:", strikes)
        print()
        guess = input("Please guess a letter: ").lower().strip()
        strikes = check_guess(strikes, guess, selected_word, guessed_letters)
        if all(letter in guessed_letters for letter in selected_word):
            print("\nCongratulations!")
            print("You guessed the correct word:", selected_word)
            return

    print("Three strikes! You are out!")


if __name__ == "__main__":
    start_game()