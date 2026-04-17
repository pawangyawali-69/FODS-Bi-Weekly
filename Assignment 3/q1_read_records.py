"""
Program to read and display contents of a CSV file.

Reads the file 'records.csv' and displays its contents. The fields
read are: student_name, roll_no, program, year, and group.
"""

import csv


FILENAME = "records.csv"
REQUIRED_FIELDS = ["student_name", "roll_no", "program", "year", "group"]


def read_records_from_csv(filename):
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            if not reader.fieldnames:
                print("\n----------------------------------------------------")
                print("  ERROR: CSV file is empty or missing headers.")
                print("----------------------------------------------------")
                return None

            missing = set(REQUIRED_FIELDS) - set(reader.fieldnames)
            if missing:
                print("\n----------------------------------------------------")
                print(f"  ERROR: Missing fields - {', '.join(missing)}")
                print("----------------------------------------------------")
                return None

            return list(reader)

    except FileNotFoundError:
        print("\n----------------------------------------------------")
        print(f"  ERROR: File not found - {filename}")
        print("----------------------------------------------------")
        return None
    except Exception as e:
        print("\n----------------------------------------------------")
        print(f"  ERROR: Error reading file - {e}")
        print("----------------------------------------------------")
        return None


def display_records(records):
    if records is None:
        return

    col_widths = {}
    for field in REQUIRED_FIELDS:
        col_widths[field] = max(len(field), max(len(row.get(field, '')) for row in records))

    print("\n" + "=" * 70)
    print("                        STUDENT RECORDS")
    print("=" * 70)
    print()
    header = "  " + " | ".join(f"{field:<{col_widths[field]}}" for field in REQUIRED_FIELDS)
    print(header)
    print("  " + "-" * 70)

    for row in records:
        print("  " + " | ".join(f"{row.get(field, ''):<{col_widths[field]}}" for field in REQUIRED_FIELDS))
    
    print("=" * 70)
    print(f"  Total Records: {len(records)}")
    print("=" * 70)


def main():
    print("\n" + "=" * 70)
    print("              CSV FILE READER PROGRAM")
    print("=" * 70)
    print()
    
    records = read_records_from_csv(FILENAME)
    display_records(records)


if __name__ == "__main__":
    main()