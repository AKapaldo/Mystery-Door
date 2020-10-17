"""
Author: Andrew Kapaldo
Date: September 21, 2020
Version 1.0
Python 3.8
"""

valid = False
print("Welcome to the Mystery Door Game!")
print("Select a door from 1-10 and and get a prize!")
while not valid:
    selection = input("What door do you choose?: ")
    print("\nWhat's behind door number", selection, "?")
    if selection == "1":
        print("You won a single left shoe!")
        valid = True
    elif selection == "2":
        print("You won a Atari 2600!")
        valid = True
    elif selection == "3":
        print("You won an all expenses paid vacation to Clarksburg!")
        valid = True
    elif selection == "4":
        print("You won a box of stale saltines!")
        valid = True
    elif selection == "5":
        print("You won a mystery novel missing the final chapter!")
        valid = True
    elif selection == "6":
        print("You won a box full of spiders!")
        valid = True
    elif selection == "7":
        print("You won a new car!")
        valid = True
    elif selection == "8":
        print("You won a $1 gift card to the Wonder Bar!")
        valid = True
    elif selection == "9":
        print("You won a Nokia 5110 phone!")
        valid = True
    elif selection == "10":
        print("You won a fully depleted AA battery!")
        valid = True
    else:
        print("Invalid Entry. Pick a number between 1 and 10.")
