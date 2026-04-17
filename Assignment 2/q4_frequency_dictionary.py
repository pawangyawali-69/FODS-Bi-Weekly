"""
Program to create a frequency dictionary from a list of numbers.

This module provides a function that takes a list of numbers as input
and returns a dictionary showing how many times each number occurs.
"""


def frequency_dictionary(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


def display_result(test_list, result):
    print()
    print(f"  Input List : {test_list}")
    print(f"  Frequency  : {result}")


def main():
    print("\n" + "=" * 50)
    print("       FREQUENCY DICTIONARY PROGRAM")
    print("=" * 50)
    print()
    print("  Testing with three different lists:")
    print("-" * 50)
    
    list1 = [1, 2, 2, 3, 3, 3]
    print("  Test Case 1:")
    display_result(list1, frequency_dictionary(list1))
    print()
    
    list2 = [4, 4, 5, 6, 6, 6, 6]
    print("  Test Case 2:")
    display_result(list2, frequency_dictionary(list2))
    print()
    
    list3 = [7, 8, 9]
    print("  Test Case 3:")
    display_result(list3, frequency_dictionary(list3))
    print()
    print("=" * 50)


if __name__ == "__main__":
    main()