"""
Program to create a number guessing game.

The computer generates a random number between 1 and 50.
The user must guess the number. After each guess, the program
tells the user whether the guess is too high, too low, or correct.
The user gets a maximum of 7 attempts. If the user does not guess
correctly within the attempts, display "Better luck next time!" and end the game.
"""

import random


def play_game():
    number = random.randint(1, 50)
    max_attempts = 7
    
    print("\n" + "=" * 50)
    print("       NUMBER GUESSING GAME")
    print("=" * 50)
    print()
    print("  I'm thinking of a number between 1 and 50.")
    print(f"  You have {max_attempts} attempts to guess it.")
    print()
    print("=" * 50)
    print()
    
    for attempt in range(1, max_attempts + 1):
        attempts_left = max_attempts - attempt + 1
        
        while True:
            try:
                user_input = input(f"  Attempt {attempt}/{max_attempts} - Enter your guess : ").strip()
                guess = int(user_input)
                
                if guess < 1 or guess > 50:
                    print("\n  ERROR: Please enter a number between 1 and 50.\n")
                    continue
                
                break
            except ValueError:
                print("\n  ERROR: Invalid input! Please enter a number.\n")
        
        print()
        
        if guess == number:
            print("=" * 50)
            print(f"  CONGRATULATIONS!")
            print(f"  You guessed the number correctly in {attempt} attempt(s)!")
            print(f"  Score: {max(0, (max_attempts - attempt + 1) * 10)}/70 points")
            print("=" * 50)
            break
        elif guess < number:
            print(f"  TOO LOW! Try higher. ({attempts_left - 1} attempts left)")
            print()
        else:
            print(f"  TOO HIGH! Try lower. ({attempts_left - 1} attempts left)")
            print()
        
        if attempt == max_attempts:
            print("=" * 50)
            print("  GAME OVER!")
            print(f"  The number was: {number}")
            print("  Better luck next time!")
            print("=" * 50)
    
    print()
    play_again = input("  Do you want to play again? (yes/no) : ").strip().lower()
    print()
    if play_again in ['yes', 'y']:
        play_game()
    else:
        print("  Thank you for playing! Goodbye!")


if __name__ == "__main__":
    play_game()