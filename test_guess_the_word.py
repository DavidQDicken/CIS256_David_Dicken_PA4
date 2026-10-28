# David Dicken
# CIS256 Fall 2026
# Programming Assignment 4

"""
This program tests the functions in the word guessing game using Pytest.
"""


# Importing functions and word list.
from guess_the_word import words, display_word_status, check_guess


# Testing if word list contains expected words.
def test_word_list():
    assert "music" in words
    assert "school" in words
    assert "garage" in words
    assert "sky" in words
    assert "banana" in words


# Testing if unguessed letters are hidden.
def test_display_word_status():
    assert display_word_status("banana", ["a"]) == "_a_a_a"


# Testing if a correct guess does not increase strikes.
def test_correct_guess():
    guessed_letters = []
    strikes = check_guess(0, "a", "banana", guessed_letters)
    assert strikes == 0
    assert "a" in guessed_letters


# Testing if an incorrect guess increases strikes.
def test_incorrect_guess():
    guessed_letters = []
    strikes = check_guess(0, "z", "banana", guessed_letters)
    assert strikes == 1
    assert "z" in guessed_letters


# Testing if guessing same letter twice does not increase strikes.
def test_duplicate_guess():
    guessed_letters = ["z"]
    strikes = check_guess(1, "z", "banana", guessed_letters)
    assert strikes == 1


# Testing if invalid input does not increase strikes.
def test_invalid_guess():
    guessed_letters = []
    strikes = check_guess(0, "12", "banana", guessed_letters)
    assert strikes == 0
    assert guessed_letters == []