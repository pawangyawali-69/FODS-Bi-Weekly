"""
Program to create a dice guessing game.

The dice has values from 1 to 6. The program generates a random value
for the dice roll. The player guesses the dice value. If the guess is
correct, shows a smiling face. If the guess is off by 1, shows a neutral face.
"""

import random


def roll_dice():
    return random.randint(1, 6)


def get_user_guess():
    try:
        return int(input("  Guess the dice value (1 to 6) : "))
    except ValueError:
        print("\n  ERROR: Invalid input. Please enter a number between 1 and 6.")
        return None


def display_result(dice, guess):
    print("\n" + "=" * 40)
    print("         DICE GUESSING GAME RESULT")
    print("=" * 40)
    print()
    print(f"  Dice Value  : {dice}")
    print(f"  Your Guess  : {guess}")
    print("-" * 40)
    
    if guess == dice:
        print("  Result      : CORRECT! You win! ")
    elif abs(guess - dice) == 1:
        print("  Result      : CLOSE! You were off by 1. ")
    else:
        print("  Result      : WRONG! Try again. ")
    
    print("=" * 40)


def main():
    print("\n" + "=" * 40)
    print("       DICE GUESSING GAME")
    print("=" * 40)
    print()
    print("  The dice has values from 1 to 6.")
    print("  Guess the dice value to win!")
    print()
    
    dice = roll_dice()
    guess = get_user_guess()
    
    if guess is not None:
        display_result(dice, guess)
    else:
        print("\n----------------------------------------------------")
        print("  ERROR: Invalid input. Please enter a number between 1 and 6.")
        print("----------------------------------------------------")


if __name__ == "__main__":
    main()