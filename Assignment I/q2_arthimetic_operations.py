"""
Program to perform basic arithmetic operations on two integers.

Takes two integer inputs from the user and displays the results of
addition, multiplication, division, modulus, and exponentiation.
"""


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def perform_arithmetic(num1, num2):
    return {
        "addition": num1 + num2,
        "multiplication": num1 * num2,
        "division": num1 / num2,
        "modulus": num1 % num2,
        "exponentiation": num1 ** num2
    }


def display_results(num1, num2, results):
    print("\n" + "=" * 50)
    print("       ARITHMETIC OPERATIONS RESULTS")
    print("=" * 50)
    print()
    print(f"  I.   Addition         : {num1} + {num2} = {results['addition']}")
    print(f"  II.  Multiplication   : {num1} x {num2} = {results['multiplication']}")
    print(f"  III. Division         : {num1} / {num2} = {results['division']:.2f}")
    print(f"  IV.  Modulus          : {num1} % {num2} = {results['modulus']}")
    print(f"  V.   Exponentiation   : {num1} ^ {num2} = {results['exponentiation']}")
    print()
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("       ARITHMETIC OPERATIONS PROGRAM")
    print("=" * 50)
    print()
    
    num1 = get_integer_input("Enter first integer  : ")
    print()
    num2 = get_integer_input("Enter second integer : ")
    print()
    
    results = perform_arithmetic(num1, num2)
    display_results(num1, num2, results)


if __name__ == "__main__":
    main()