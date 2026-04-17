"""
Program to implement mathematical operations using separate functions.

This module provides functions for addition, multiplication, division,
floor division, and exponentiation. Each function takes two inputs,
performs the operation, and returns the result.
"""


def addition(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Undefined (division by zero)"
    return a / b


def floor_division(a, b):
    if b == 0:
        return "Undefined (division by zero)"
    return a // b


def exponentiation(a, b):
    return a ** b


def get_float_input(prompt):
    return float(input(prompt))


def display_results(num1, num2):
    print("\n" + "=" * 50)
    print("         MATHEMATICAL OPERATIONS RESULTS")
    print("=" * 50)
    print()
    print(f"  Number 1 : {num1}")
    print(f"  Number 2 : {num2}")
    print("-" * 50)
    print()
    print(f"  I.   Addition         : {addition(num1, num2)}")
    print(f"  II.  Multiplication   : {multiplication(num1, num2)}")
    
    div_result = division(num1, num2)
    if isinstance(div_result, str):
        print(f"  III. Division         : {div_result}")
    else:
        print(f"  III. Division         : {div_result:.2f}")
    
    fdiv_result = floor_division(num1, num2)
    if isinstance(fdiv_result, str):
        print(f"  IV.  Floor Division  : {fdiv_result}")
    else:
        print(f"  IV.  Floor Division  : {fdiv_result}")
    
    print(f"  V.   Exponentiation  : {exponentiation(num1, num2)}")
    print()
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("       MATHEMATICAL OPERATIONS PROGRAM")
    print("=" * 50)
    print()
    
    try:
        num1 = get_float_input("Enter the first number  : ")
        print()
        num2 = get_float_input("Enter the second number : ")
        print()
        display_results(num1, num2)
    except ValueError:
        print("\n----------------------------------------------------")
        print("  ERROR: Invalid input. Please enter numeric values.")
        print("----------------------------------------------------")


if __name__ == "__main__":
    main()