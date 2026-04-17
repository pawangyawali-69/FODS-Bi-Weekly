"""
Program to create a Learner class and demonstrate its usage.

Creates a class Learner with attributes: roll_no, full_name, address,
enrollment_year, program, and group. Instantiates an object of the class
to take input for all attributes and display the details.
"""


class Learner:
    def __init__(self, roll_no, full_name, address, enrollment_year, program, group):
        self.roll_no = roll_no
        self.full_name = full_name
        self.address = address
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    def __str__(self):
        return (
            f"\n{'=' * 45}\n"
            f"          LEARNER DETAILS\n"
            f"{'=' * 45}\n"
            f"  Roll No         : {self.roll_no}\n"
            f"  Full Name       : {self.full_name}\n"
            f"  Address         : {self.address}\n"
            f"  Enrollment Year : {self.enrollment_year}\n"
            f"  Program         : {self.program}\n"
            f"  Group           : {self.group}\n"
            f"{'=' * 45}"
        )


def get_valid_year(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return value
        print("\n  ERROR: Please enter a valid year (numbers only).")


def get_learner_input():
    print("  Enter Learner Details:")
    print("  " + "-" * 35)
    
    roll_no = input("  Roll No         : ").strip()
    full_name = input("  Full Name       : ").strip()
    address = input("  Address         : ").strip()
    enrollment_year = get_valid_year("  Enrollment Year : ")
    program = input("  Program         : ").strip()
    group = input("  Group           : ").strip()

    return Learner(roll_no, full_name, address, enrollment_year, program, group)


def main():
    print("\n" + "=" * 45)
    print("       LEARNER CLASS PROGRAM")
    print("=" * 45)
    print()
    
    learner = get_learner_input()
    print(learner)


if __name__ == "__main__":
    main()