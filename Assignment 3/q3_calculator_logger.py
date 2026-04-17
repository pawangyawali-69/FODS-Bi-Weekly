"""
Program to perform calculator operations and log results to a file.

Accepts a list of integers from the user, performs addition, subtraction,
multiplication, and division operations, and saves the results into a file
with the current date and time. The program continues until the user
decides to exit, then displays the file contents in a formatted way.
"""

import datetime
import os


FILENAME = "calculator_log.txt"


def get_integer_list():
    while True:
        raw = input("  Enter integers (or type 'exit' to quit) : ").strip()

        if raw.lower() == "exit":
            return None

        try:
            numbers = list(map(int, raw.split()))
            if len(numbers) == 0:
                print("\n  ERROR: Please enter at least one number.")
                continue
            return numbers
        except ValueError:
            print("\n  ERROR: Invalid input! Please enter only integers.")


def calculate_operations(numbers):
    result = {}

    result["addition"] = sum(numbers)

    sub = numbers[0]
    for n in numbers[1:]:
        sub -= n
    result["subtraction"] = sub

    mul = 1
    for n in numbers:
        mul *= n
    result["multiplication"] = mul

    try:
        div = numbers[0]
        for n in numbers[1:]:
            div /= n
        result["division"] = round(div, 2)
    except ZeroDivisionError:
        result["division"] = "Error"

    return result


def log_to_file(numbers, result):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{now}|{numbers}|{result['addition']}|{result['subtraction']}|{result['multiplication']}|{result['division']}\n"

    with open(FILENAME, "a") as f:
        f.write(line)


def display_operations_result(result):
    print("\n  " + "-" * 40)
    print("  RESULTS:")
    print("  " + "-" * 40)
    print(f"  Addition       : {result['addition']}")
    print(f"  Subtraction    : {result['subtraction']}")
    print(f"  Multiplication : {result['multiplication']}")
    print(f"  Division       : {result['division']}")
    print("  " + "-" * 40)


def display_file_contents():
    if not os.path.exists(FILENAME):
        print("\n  No records found.")
        return

    print("\n" + "=" * 90)
    print("                          CALCULATOR LOG HISTORY")
    print("=" * 90)
    print()
    print(f"  {'DATE & TIME':20} | {'INPUTS':15} | {'ADD':8} | {'SUB':8} | {'MUL':10} | {'DIV'}")
    print("  " + "-" * 85)

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 6:
                print(f"  {parts[0]:20} | {parts[1]:15} | {parts[2]:8} | {parts[3]:8} | {parts[4]:10} | {parts[5]}")

    print("=" * 90)


def main():
    print("\n" + "=" * 50)
    print("       MULTI-OPERATION CALCULATOR")
    print("=" * 50)
    print()
    print("  Enter integers to perform calculations.")
    print("  Results will be saved to file.")
    print()

    while True:
        numbers = get_integer_list()

        if numbers is None:
            break

        result = calculate_operations(numbers)
        log_to_file(numbers, result)
        display_operations_result(result)
        print()

    display_file_contents()


if __name__ == "__main__":
    main()