"""
Program to perform arithmetic operations on two integers.

This module provides functions to calculate sum, difference, product,
and quotient of two integers entered by the user.
"""


def calculate(a, b):
    sum_val = a + b
    difference = a - b
    product = a * b
    if b != 0:
        quotient = a / b
    else:
        quotient = "Undefined (division by zero)"
    
    print("\n" + "=" * 45)
    print("          ARITHMETIC RESULTS")
    print("=" * 45)
    print()
    print(f"  Sum        : {sum_val}")
    print(f"  Difference : {difference}")
    print(f"  Product    : {product}")
    print(f"  Quotient   : {quotient}")
    print("=" * 45)


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\n  ERROR: Invalid input. Please enter a valid integer.")


def main():
    print("\n" + "=" * 45)
    print("       CALCULATOR PROGRAM")
    print("=" * 45)
    print()
    
    a = get_integer_input("Enter first integer  : ")
    print()
    b = get_integer_input("Enter second integer : ")
    
    calculate(a, b)


if __name__ == "__main__":
    main()