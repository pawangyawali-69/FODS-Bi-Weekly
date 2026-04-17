"""
Program to perform matrix operations using NumPy.

Prompts the user to input two matrices of compatible dimensions and
performs addition, subtraction, and multiplication operations. Validates
dimension compatibility before performing operations and raises proper
exceptions if matrix sizes are mismatched.
"""

import numpy as np


class DimensionMismatchError(Exception):
    pass


def input_matrix(name):
    rows = int(input(f"  Enter number of rows for {name} : "))
    cols = int(input(f"  Enter number of columns for {name} : "))

    matrix = []
    print(f"  Enter elements for {name} (row-wise):")

    for i in range(rows):
        while True:
            row_input = input(f"    Row {i + 1} : ").strip()
            row = row_input.split()
            if len(row) == cols:
                try:
                    row = list(map(float, row))
                    matrix.append(row)
                    break
                except ValueError:
                    print("    ERROR: Please enter valid numbers.")
            else:
                print(f"    ERROR: Row must have exactly {cols} elements.")

    return np.array(matrix)


def validate_dimensions_for_addition_subtraction(A, B):
    if A.shape != B.shape:
        raise DimensionMismatchError("Addition/Subtraction requires matrices of same dimensions.")


def validate_dimensions_for_multiplication(A, B):
    if A.shape[1] != B.shape[0]:
        raise DimensionMismatchError("Multiplication requires columns of A = rows of B.")


def perform_matrix_operations(A, B):
    validate_dimensions_for_addition_subtraction(A, B)

    results = {
        "addition": A + B,
        "subtraction": A - B
    }

    validate_dimensions_for_multiplication(A, B)
    results["multiplication"] = np.dot(A, B)

    return results


def display_matrices_and_results(A, B, results):
    print("\n" + "=" * 55)
    print("        MATRIX OPERATIONS RESULTS")
    print("=" * 55)
    print()
    print("  Matrix A:")
    print(A)
    print()
    print("  Matrix B:")
    print(B)
    print("-" * 55)
    print()
    print("  Addition (A + B):")
    print(results["addition"])
    print()
    print("  Subtraction (A - B):")
    print(results["subtraction"])
    print()
    print("  Multiplication (A x B):")
    print(results["multiplication"])
    print("=" * 55)


def main():
    print("\n" + "=" * 55)
    print("       MATRIX OPERATIONS PROGRAM")
    print("=" * 55)
    print()
    
    try:
        A = input_matrix("Matrix A")
        print()
        B = input_matrix("Matrix B")

        results = perform_matrix_operations(A, B)
        display_matrices_and_results(A, B, results)

    except (ValueError, DimensionMismatchError) as e:
        print("\n----------------------------------------------------")
        print(f"  ERROR: {e}")
        print("----------------------------------------------------")


if __name__ == "__main__":
    main()