"""
Program to perform various mathematical operations on a number.

Takes a single number as input and displays:
- Cube of the number
- Cube root of the number
- Natural logarithm of the number
- Base-2 logarithm of the number
- The number raised to the power of 6
"""

import math


def get_number_input(prompt):
    return float(input(prompt))


def calculate_math_operations(num):
    cube = num ** 3
    cube_root = math.copysign(abs(num) ** (1/3), num)

    if num <= 0:
        natural_log = "Undefined (non-positive)"
        log2 = "Undefined (non-positive)"
    else:
        natural_log = math.log(num)
        log2 = math.log2(num)

    power_6 = num ** 6

    return {
        "cube": cube,
        "cube_root": cube_root,
        "natural_log": natural_log,
        "log2": log2,
        "power_6": power_6
    }


def display_results(num, results):
    print("\n" + "=" * 55)
    print("            MATHEMATICAL OPERATIONS RESULTS")
    print("=" * 55)
    print()
    print(f"  Given Number : {num}")
    print("-" * 55)
    print()
    print(f"  I.   Cube of the number          : {results['cube']}")
    print(f"  II.  Cube root of the number     : {results['cube_root']:.4f}")
    
    if isinstance(results['natural_log'], str):
        print(f"  III. Natural logarithm          : {results['natural_log']}")
        print(f"  IV.  Base-2 logarithm          : {results['log2']}")
    else:
        print(f"  III. Natural logarithm          : {results['natural_log']:.4f}")
        print(f"  IV.  Base-2 logarithm          : {results['log2']:.4f}")
    
    print(f"  V.   Number raised to power 6   : {results['power_6']}")
    print()
    print("=" * 55)


def main():
    print("\n" + "=" * 55)
    print("         MATHEMATICAL OPERATIONS PROGRAM")
    print("=" * 55)
    print()
    
    try:
        num = get_number_input("Enter a number : ")
        print()
        results = calculate_math_operations(num)
        display_results(num, results)
    except ValueError:
        print("\n----------------------------------------------------")
        print("  ERROR: Invalid input. Please enter a valid number.")
        print("----------------------------------------------------")


if __name__ == "__main__":
    main()