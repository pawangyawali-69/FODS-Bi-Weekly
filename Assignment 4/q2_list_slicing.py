"""
Program to sort a list and perform slicing operations.

Prompts the user to enter at least 12 numbers, sorts the list, and
performs slicing operations to extract elements between index ranges.
"""


def get_number_list():
    while True:
        s = input("  Enter at least 12 numbers (separated by spaces) : ").strip()
        if not s:
            print("\n  ERROR: Input cannot be empty.")
            continue

        parts = s.split()

        try:
            nums = [float(x) for x in parts]
        except ValueError:
            print("\n  ERROR: Only numeric values are allowed. Try again.")
            continue

        if len(nums) < 12:
            print(f"\n  ERROR: You entered {len(nums)} numbers. Please enter at least 12.")
            continue

        return nums


def sort_list(nums):
    return sorted(nums)


def perform_slicing(nums):
    return {
        "index_3_6": nums[3:7],
        "index_6_9": nums[6:10],
        "index_4_10": nums[4:11]
    }


def display_results(nums, slices):
    print("\n" + "=" * 55)
    print("        LIST SORTING & SLICING RESULTS")
    print("=" * 55)
    print()
    print(f"  Sorted List : {nums}")
    print("-" * 55)
    print("  Slicing Results:")
    print(f"    Index 3-6   : {slices['index_3_6']}")
    print(f"    Index 6-9   : {slices['index_6_9']}")
    print(f"    Index 4-10  : {slices['index_4_10']}")
    print("=" * 55)


def main():
    print("\n" + "=" * 55)
    print("       LIST SORTING & SLICING PROGRAM")
    print("=" * 55)
    print()
    
    nums = get_number_list()
    sorted_nums = sort_list(nums)
    slices = perform_slicing(sorted_nums)
    display_results(sorted_nums, slices)


if __name__ == "__main__":
    main()