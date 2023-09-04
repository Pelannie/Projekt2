"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie: "Bulls & Cows"
author: Anna Peloušková
email: a.pelouskova@seznam.cz
discord: Pel#9400
"""

from plurals import plural
from random import randint

def generate_number():
    generated_number = randint(1023,9876)
    while (not validate_number(str(generated_number))):
        generated_number = randint(1023,9876)
    return generated_number

def validate_number(input):
    if (not input.isdigit()):
        return False
    if (len(input) != 4):
        return False
    if (input[0] == "0"):
        return False
    if (len(set(input)) != 4):
        return False
    
    return True

def bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0

    for i in range(0,4):
        if (guess[i] == secret[i]):
            bulls = bulls + 1
        elif (guess[i] in set(secret)):
            cows = cows + 1

    print(bulls, plural(bulls, "bull") + ",",cows, plural(cows, "cow"))
    return

def conclusion(guesses_count):
    if (guesses_count <= 5):
        return "amazing"
    if (guesses_count <= 10):
        return "average"
    if (guesses_count <= 15):
        return "not so good"
    if (guesses_count <= 20):
        return "below average"
    else:
        return "way below average"

print("Hi there!")
print("-----------------------------------------------")

guessed_number = generate_number()

print("I've generated a random 4 digit number for you.")
# print(guessed_number)
print("Let's play a bulls and cows game.")
print("-----------------------------------------------")
print("Enter a number:")
print("-----------------------------------------------")

user_guess = 0
guesses = 0

while (guessed_number != int(user_guess)):
    print(">>> ", end = "")
    user_guess = input()
    if not validate_number(user_guess):
        print("Your guess", user_guess, 
              "is not valid input.",
              "It has to be a four digit number",
              "not starting with zero",
              "and without repeating digits.")
        user_guess = 0
        continue

    guesses = guesses + 1
    if (guessed_number != int(user_guess)):
        bulls_and_cows(str(guessed_number), user_guess)
        print("-----------------------------------------------")

print("Correct, you've guessed the right number")
print("in", guesses, plural(guesses, "guess")+"!")
print("-----------------------------------------------")
print("That's", conclusion(guesses) + ".")