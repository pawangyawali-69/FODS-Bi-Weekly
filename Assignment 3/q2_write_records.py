"""
Program to append user details to an existing CSV file.

Prompts the user to enter student details and appends them to
'records.csv'. The fields taken are: student_name, roll_no,
program, year, and group.
"""

import csv
import os


FILENAME = "records.csv"
REQUIRED_FIELDS = ["student_name", "roll_no", "program", "year", "group"]


def get_student_data():
    print("  Enter student details:")
    print("  " + "-" * 35)
    return {
        "student_name": input("  Student Name  : ").strip(),
        "roll_no": input("  Roll Number   : ").strip(),
        "program": input("  Program       : ").strip(),
        "year": input("  Year          : ").strip(),
        "group": input("  Group         : ").strip()
    }


def append_record_to_csv(filename, data):
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=REQUIRED_FIELDS)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)


def get_user_choice(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        print("\n  ERROR: Please enter 'yes' or 'no'.")


def display_success():
    print("\n" + "=" * 45)
    print("         RECORD ADDED SUCCESSFULLY")
    print("=" * 45)


def main():
    print("\n" + "=" * 45)
    print("       CSV FILE WRITER PROGRAM")
    print("=" * 45)
    print()
    
    while True:
        data = get_student_data()
        append_record_to_csv(FILENAME, data)
        display_success()
        
        print()
        if not get_user_choice("  Do you want to add another record? (yes/no) : "):
            print("\n  Exiting... Thank you!")
            break
        print()


if __name__ == "__main__":
    main()