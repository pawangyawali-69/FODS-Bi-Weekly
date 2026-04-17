"""
Program to remove duplicates from a list of numbers and sort them.

Prompts the user to enter numbers separated by spaces, removes
duplicates, and returns the numbers sorted in ascending order.
"""


def remove_duplicates_and_sort(numbers):
    return sorted(set(numbers))


def get_number_list_input(prompt):
    user_input = input(prompt)
    if user_input.strip():
        return list(map(int, user_input.split()))
    return []


def display_result(numbers, result):
    print("\n" + "=" * 50)
    print("       REMOVE DUPLICATES & SORT RESULT")
    print("=" * 50)
    print()
    print(f"  Original List      : {numbers}")
    print(f"  After removing dup : {result}")
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("    REMOVE DUPLICATES & SORT PROGRAM")
    print("=" * 50)
    print()
    
    numbers = get_number_list_input("  Enter numbers separated by spaces : ")
    
    if not numbers:
        print("\n----------------------------------------------------")
        print("  ERROR: No numbers entered.")
        print("----------------------------------------------------")
        return
    
    result = remove_duplicates_and_sort(numbers)
    display_result(numbers, result)


if __name__ == "__main__":
    main()