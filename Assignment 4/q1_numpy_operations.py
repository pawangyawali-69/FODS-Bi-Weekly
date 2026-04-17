"""
Program to perform array operations using NumPy.

Creates a NumPy array and performs the following operations:
- Find the total sum of elements
- Calculate the mean value of the array
- Identify the largest and smallest values in the array
"""

import numpy as np


def create_array():
    return np.array([10, 20, 30, 40, 50])


def perform_array_operations(arr):
    return {
        "total_sum": np.sum(arr),
        "mean_value": np.mean(arr),
        "max_value": np.max(arr),
        "min_value": np.min(arr)
    }


def display_results(arr, results):
    print("\n" + "=" * 50)
    print("        NUMPY ARRAY OPERATIONS RESULTS")
    print("=" * 50)
    print()
    print(f"  Array       : {arr}")
    print("-" * 50)
    print(f"  Total Sum   : {results['total_sum']}")
    print(f"  Mean Value  : {results['mean_value']}")
    print(f"  Max Value   : {results['max_value']}")
    print(f"  Min Value   : {results['min_value']}")
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("       NUMPY ARRAY OPERATIONS PROGRAM")
    print("=" * 50)
    print()
    
    arr = create_array()
    results = perform_array_operations(arr)
    display_results(arr, results)


if __name__ == "__main__":
    main()