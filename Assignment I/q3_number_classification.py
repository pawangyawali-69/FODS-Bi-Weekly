"""
Program to classify a number as positive/negative and even/odd.

Prompts the user to enter a number and determines whether it is:
- Positive, even
- Positive odd
- Negative even
- Negative odd
- Zero
- Non-integer numbers
"""


def get_number_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("\n----------------------------------------------------")
        print("  ERROR: Invalid input. Please enter a numeric value.")
        print("----------------------------------------------------")
        raise SystemExit(1)


def classify_number(num):
    if num == 0:
        return "Zero is neither positive nor negative. It is even."
    elif num > 0:
        if num.is_integer() and int(num) % 2 == 0:
            return "Positive Even"
        elif num.is_integer():
            return "Positive Odd"
        else:
            return "Positive (Non-integer Number)"
    else:
        if num.is_integer() and int(num) % 2 == 0:
            return "Negative Even"
        elif num.is_integer():
            return "Negative Odd"
        else:
            return "Negative (Non-integer Number)"


def main():
    print("\n" + "=" * 50)
    print("       NUMBER CLASSIFICATION PROGRAM")
    print("=" * 50)
    print()
    
    num = get_number_input("Enter a number : ")
    print()
    
    result = classify_number(num)
    
    print("\n" + "-" * 50)
    print("  RESULT")
    print("-" * 50)
    print(f"  The number {num} is classified as : {result}")
    print("-" * 50)


if __name__ == "__main__":
    main()