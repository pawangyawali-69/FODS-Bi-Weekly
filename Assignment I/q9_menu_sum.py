"""
Menu-driven program to compute separate sums of positive and negative numbers.
Repeatedly asks the user for numbers and computes the sum of positive and negative numbers.
Continues until the user chooses to exit.
"""


class NumberAccumulator:
    def __init__(self):
        self.positive_sum = 0.0
        self.negative_sum = 0.0

    def add_number(self, number):
        if number > 0:
            self.positive_sum += number
        elif number < 0:
            self.negative_sum += number

    def get_sums(self):
        return self.positive_sum, self.negative_sum


def display_menu():
    print("\n" + "-" * 40)
    print("           MENU")
    print("-" * 40)
    print("  1. Enter a number")
    print("  2. View sums")
    print("  3. Exit")
    print("-" * 40)


def get_menu_choice():
    return input("  Enter your choice : ").strip()


def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ERROR: Please enter a valid number.")


def process_choice(choice, accumulator):
    if choice == "1":
        num = get_number_input("  Enter a number : ")
        accumulator.add_number(num)

    elif choice == "2":
        pos_sum, neg_sum = accumulator.get_sums()
        print("\n" + "-" * 40)
        print("           SUMS RESULT")
        print("-" * 40)
        print(f"  Sum of Positive Numbers : {pos_sum}")
        print(f"  Sum of Negative Numbers : {neg_sum}")
        print("-" * 40)

    elif choice == "3":
        return True

    else:
        print("\n  ERROR: Invalid choice. Please enter 1, 2, or 3.")

    return False


def main():
    print("\n" + "=" * 40)
    print("     POSITIVE/NEGATIVE SUM CALCULATOR")
    print("=" * 40)

    accumulator = NumberAccumulator()

    while True:
        display_menu()
        choice = get_menu_choice()

        if process_choice(choice, accumulator):
            print("\n  Thank you! Exiting program...")
            break


if __name__ == "__main__":
    main()