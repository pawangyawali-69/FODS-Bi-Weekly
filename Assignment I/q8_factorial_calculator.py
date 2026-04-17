"""
Program to compute the factorial of a number entered by the user.

Ensures the input is a valid positive integer. If the user enters
anything else, displays an error message.
"""


def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)


def get_valid_positive_integer(prompt):
    user_input = input(prompt)
    try:
        num = int(user_input)
        if num < 0:
            raise ValueError("Negative number")
        return num
    except ValueError:
        raise ValueError("Invalid input")


def display_result(num, fact):
    print("\n" + "=" * 45)
    print("        FACTORIAL CALCULATION RESULT")
    print("=" * 45)
    print()
    print(f"  Number          : {num}")
    print(f"  Factorial       : {fact}")
    print()
    print("=" * 45)


def main():
    print("\n" + "=" * 45)
    print("        FACTORIAL CALCULATOR PROGRAM")
    print("=" * 45)
    print()
    
    try:
        num = get_valid_positive_integer("Enter a positive integer : ")
        print()
        fact = calculate_factorial(num)
        display_result(num, fact)
    except ValueError:
        print("\n----------------------------------------------------")
        print("  ERROR: Invalid input! Please enter a positive integer.")
        print("----------------------------------------------------")


if __name__ == "__main__":
    main()