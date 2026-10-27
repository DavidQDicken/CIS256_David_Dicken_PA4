# David Dicken
# CIS256 Fall 2026
# Programming Assignment 4

"""
A word guessing game that allows you to keep guesing until you have made three wrong guesses.
"""


import random


words = ["music", "school", "garage", "sky", "banana"]

selected_word = random.choice(words)
guessed_letters = []
attempts = 3

print("Guess the word using one letter at a time.")

while attempts > 0:
    print()
    print(selected_word)
    print("You have", attempts, "attempts remaining.\n")
    guess = input("Please guess a letter: ").lower().strip()
    if guess not in selected_word:
        attempts = attempts - 1
