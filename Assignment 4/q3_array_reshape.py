"""
Program to create, sort, and reshape a NumPy array.

Generates an array of 12 random integers, sorts them, and reshapes
the array into a valid matrix dimension (3x4 or 4x3).
"""

import numpy as np


def generate_random_array(size=12):
    return np.random.randint(0, 100, size)


def sort_array(arr):
    return np.sort(arr)


def reshape_array(arr, rows=3, cols=4):
    return arr.reshape(rows, cols)


def display_results(original_arr, sorted_arr, matrix):
    print("\n" + "=" * 55)
    print("        ARRAY GENERATE, SORT & RESHAPE")
    print("=" * 55)
    print()
    print(f"  Original Array : {original_arr}")
    print("-" * 55)
    print(f"  Sorted Array   : {sorted_arr}")
    print("-" * 55)
    print(f"  Reshaped Matrix (3x4):")
    print()
    print(matrix)
    print("=" * 55)


def main():
    print("\n" + "=" * 55)
    print("       ARRAY RESHAPE PROGRAM")
    print("=" * 55)
    print()
    
    arr = generate_random_array(12)
    sorted_arr = sort_array(arr)
    matrix = reshape_array(sorted_arr)
    display_results(arr, sorted_arr, matrix)


if __name__ == "__main__":
    main()