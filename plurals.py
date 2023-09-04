"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie: "Bulls & Cows"
author: Anna Peloušková
email: a.pelouskova@seznam.cz
discord: Pel#9400
"""

iregular_plurals = {
            "guess": "guesses",
            "mouse": "mice"
        }

def plural(number, noun):
    if (number == 1):
        return noun
    else:
        if (noun in iregular_plurals):
            return iregular_plurals[noun]
        else:
            return noun + "s" 