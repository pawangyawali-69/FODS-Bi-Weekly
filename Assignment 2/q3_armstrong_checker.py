"""
Program to check if a string represents an Armstrong number.

An Armstrong number (also known as narcissistic number) is a number
that is equal to the sum of its own digits each raised to the power
of the number of digits.
"""


def is_armstrong(s):
    try:
        num = int(s)
        digits = [int(d) for d in s]
        n = len(digits)
        sum_pow = sum(d ** n for d in digits)
        return sum_pow == num
    except ValueError:
        return False


def get_user_input(prompt):
    return input(prompt)


def display_result(s, is_armstrong_num):
    print("\n" + "=" * 45)
    print("       ARMSTRONG NUMBER CHECKER")
    print("=" * 45)
    print()
    print(f"  Input Number : {s}")
    print("-" * 45)
    
    if is_armstrong_num:
        print(f"  Result       : {s} IS an Armstrong number")
    else:
        print(f"  Result       : {s} is NOT an Armstrong number")
    
    print("=" * 45)


def main():
    print("\n" + "=" * 45)
    print("       ARMSTRONG NUMBER CHECKER")
    print("=" * 45)
    print()
    
    s = get_user_input("Enter a number : ")
    print()
    
    result = is_armstrong(s)
    display_result(s, result)


if __name__ == "__main__":
    main()