# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sept 2021
# This program asks the user to ask a number between 0-9


import random


def main():
    # this function checks if the user picked the computer generated number

    # input
    die = random.randint(0, 9)  # a number between 0 and 9
    number = int(input("Guess a number between 0-9: "))
    print("")

    # process & output
    if number != die:
        print("You guessed incorrectly.")

    else:
        print("You guessed correctly!")

    print("\nDone.")


if __name__ == "__main__":
    main()
