"""
Program to find numbers divisible by 9 but not by 6 in a given range.

Prompts the user for the start and end of the range, then displays
all numbers that are divisible by 9 but not divisible by 6.
"""

DIVISIBILITY_RULES = {
    "divisible_by_9": 9,
    "not_divisible_by_6": 6
}


def get_range_from_user():
    print("\n  Enter the range limits:")
    start = int(input("  Start of range  : "))
    end = int(input("  End of range    : "))
    return start, end


def find_divisible_numbers(start, end):
    return [
        num for num in range(start, end + 1)
        if num % DIVISIBILITY_RULES["divisible_by_9"] == 0
        and num % DIVISIBILITY_RULES["not_divisible_by_6"] != 0
    ]


def display_results(start, end, numbers):
    print("\n" + "=" * 55)
    print("       NUMBERS DIVISIBLE BY 9 BUT NOT BY 6")
    print("=" * 55)
    print()
    print(f"  Range : {start} to {end}")
    print("-" * 55)
    print("  Numbers:")
    
    if numbers:
        for num in numbers:
            print(f"    {num}")
    else:
        print("    No numbers found in this range.")
    
    print("-" * 55)
    print(f"  Total Count : {len(numbers)}")
    print("=" * 55)


def main():
    print("\n" + "=" * 55)
    print("       DIVISIBILITY FINDER PROGRAM")
    print("=" * 55)
    
    start, end = get_range_from_user()
    numbers = find_divisible_numbers(start, end)
    display_results(start, end, numbers)


if __name__ == "__main__":
    main()