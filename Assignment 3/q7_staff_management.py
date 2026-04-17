"""
Program to create a Staff class and manage staff data.

Creates a Staff class with attributes: emp_id, full_name, address,
phone_number, marital_status, dependents, and salary. Instantiates
this class for multiple staff members and writes the data into a file
'staff.csv'. The program also allows the user to view the list of
staff and their details. Uses try/except for exception handling.
"""

import csv
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


FILENAME = "staff.csv"


class Staff:
    def __init__(self, emp_id, full_name, address, phone_number, marital_status, dependents, salary):
        self.emp_id = emp_id
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.marital_status = marital_status
        self.dependents = dependents
        self.salary = salary


def load_from_csv(filename):
    staff_list = []
    try:
        if not os.path.exists(filename):
            return staff_list
        
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                staff = Staff(
                    row["Employee ID"],
                    row["Full Name"],
                    row["Address"],
                    row["Phone Number"],
                    row["Marital Status"],
                    row["Dependents"],
                    row["Salary"]
                )
                staff_list.append(staff)
    except Exception:
        pass
    return staff_list


def save_to_csv(staff_list, filename):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Employee ID", "Full Name", "Address",
                "Phone Number", "Marital Status", "Dependents", "Salary"
            ])

            for staff in staff_list:
                writer.writerow([
                    staff.emp_id,
                    staff.full_name,
                    staff.address,
                    staff.phone_number,
                    staff.marital_status,
                    staff.dependents,
                    staff.salary
                ])

        return True

    except Exception as e:
        print("\n----------------------------------------------------")
        print(f"  ERROR: Error writing file - {e}")
        print("----------------------------------------------------")
        return False


def view_staff(staff_list):
    if not staff_list:
        print("\n" + "=" * 80)
        print("  No staff records found.")
        print("=" * 80)
        return

    col_widths = [10, 18, 18, 14, 14, 11, 12]
    total_width = sum(col_widths) + (3 * 6) + 2
    
    print("\n" + "=" * total_width)
    print("                              STAFF DETAILS".center(total_width))
    print("=" * total_width)
    
    header = "  " + " | ".join([
        f"{'Emp ID':<{col_widths[0]}}",
        f"{'Full Name':<{col_widths[1]}}",
        f"{'Address':<{col_widths[2]}}",
        f"{'Phone':<{col_widths[3]}}",
        f"{'Status':<{col_widths[4]}}",
        f"{'Dependents':<{col_widths[5]}}",
        f"{'Salary':<{col_widths[6]}}"
    ])
    print(header)
    print("-" * total_width)
    
    for staff in staff_list:
        print("  " + " | ".join([
            f"{staff.emp_id:<{col_widths[0]}}",
            f"{staff.full_name:<{col_widths[1]}}",
            f"{staff.address:<{col_widths[2]}}",
            f"{staff.phone_number:<{col_widths[3]}}",
            f"{staff.marital_status:<{col_widths[4]}}",
            f"{staff.dependents:<{col_widths[5]}}",
            f"{staff.salary:<{col_widths[6]}}"
        ]))
    
    print("=" * total_width)
    print(f"  Total Staff: {len(staff_list)}")
    print("=" * total_width)


def add_staff(staff_list):
    clear_screen()
    print("\n" + "=" * 60)
    print("           ADD NEW STAFF")
    print("=" * 60)
    print("\n  Enter staff details:")
    print("  " + "-" * 40)
    
    emp_id = input("  Employee ID    : ").strip()
    name = input("  Full Name      : ").strip()
    address = input("  Address        : ").strip()
    phone = input("  Phone Number   : ").strip()
    marital = input("  Marital Status : ").strip()
    dependents = input("  Dependents     : ").strip()
    salary = input("  Salary         : ").strip()
    
    staff = Staff(emp_id, name, address, phone, marital, dependents, salary)
    staff_list.append(staff)
    
    if save_to_csv(staff_list, FILENAME):
        print("\n" + "=" * 60)
        print("  Staff added and saved successfully!")
        print("=" * 60)


def display_menu():
    clear_screen()
    print("\n" + "=" * 60)
    print("       STAFF MANAGEMENT PROGRAM")
    print("=" * 60)
    print("  1. View All Staff")
    print("  2. Add New Staff")
    print("  3. Exit")
    print("=" * 60)


def main():
    clear_screen()
    print("\n" + "=" * 60)
    print("       STAFF MANAGEMENT PROGRAM")
    print("=" * 60)
    
    staff_list = load_from_csv(FILENAME)
    if staff_list:
        print(f"\n  Loaded {len(staff_list)} staff record(s).")
    
    while True:
        display_menu()
        choice = input("  Enter your choice : ").strip()
        
        if choice == "1":
            clear_screen()
            view_staff(staff_list)
        elif choice == "2":
            add_staff(staff_list)
        elif choice == "3":
            clear_screen()
            print("\n" + "=" * 60)
            print("  Exiting program... Thank you!")
            print("=" * 60)
            break
        else:
            clear_screen()
            print("\n" + "=" * 60)
            print("  Invalid choice!")
            print("=" * 60)
        
        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()