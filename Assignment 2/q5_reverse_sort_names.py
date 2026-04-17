"""
Program to sort student names in reverse alphabetical order.

Prompts the user to enter the number of students and their names,
then displays the names sorted in reverse alphabetical order.
"""


def sort_names_reverse(names):
    return sorted(names, reverse=True)


def get_ordinal_suffix(n):
    if n == 0:
        return "1st"
    elif n == 1:
        return "2nd"
    elif n == 2:
        return "3rd"
    else:
        return f"{n + 1}th"


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("\n  ERROR: Please enter a positive number.")
        except ValueError:
            print("\n  ERROR: Invalid input. Please enter a valid number.")


def get_student_names(n):
    names = []
    for i in range(n):
        name = input(f"  Enter name of {get_ordinal_suffix(i)} student : ")
        names.append(name)
    return names


def display_results(students, sorted_students):
    print("\n" + "=" * 50)
    print("           SORTED NAMES RESULT")
    print("=" * 50)
    print()
    print(f"  Original List                  : {students}")
    print(f"  Sorted (Reverse Alphabetical)  : {sorted_students}")
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("       REVERSE ALPHABETICAL SORT PROGRAM")
    print("=" * 50)
    print()
    
    n = get_positive_integer("  Enter number of students : ")
    print()
    students = get_student_names(n)
    sorted_students = sort_names_reverse(students)
    
    display_results(students, sorted_students)


if __name__ == "__main__":
    main()