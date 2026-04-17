"""
Program to calculate total, average, percentage, and grade.

Prompts the user to enter marks for 6 subjects and calculates:
- Total marks
- Average marks
- Percentage
- Grade based on percentage thresholds
"""

GRADE_THRESHOLDS = [
    (85, "Distinction"),
    (70, "First Division"),
    (55, "Second Division"),
    (45, "Third Division"),
    (0, "Fail")
]


def get_valid_mark(subject_num):
    while True:
        try:
            mark = float(input(f"  Enter marks for Subject {subject_num} : "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("\n  ERROR: Marks should be between 0 and 100. Try again.")
        except ValueError:
            print("\n  ERROR: Invalid input. Please enter a number.")


def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    percentage = average

    for threshold, grade in GRADE_THRESHOLDS:
        if percentage >= threshold:
            return {
                "total": total,
                "average": average,
                "percentage": percentage,
                "grade": grade
            }

    return {
        "total": total,
        "average": average,
        "percentage": percentage,
        "grade": "Fail"
    }


def display_results(marks, results):
    print("\n" + "=" * 50)
    print("         GRADE CALCULATION RESULTS")
    print("=" * 50)
    print()
    print(f"  Marks Entered : {marks}")
    print("-" * 50)
    print(f"  Total Marks   : {results['total']}")
    print(f"  Average       : {results['average']:.2f}")
    print(f"  Percentage    : {results['percentage']:.2f}%")
    print("-" * 50)
    print(f"  Grade         : {results['grade']}")
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("         GRADE CALCULATION PROGRAM")
    print("=" * 50)
    print()
    print("  Enter marks for 6 subjects:")
    print("-" * 50)
    
    marks = [get_valid_mark(i + 1) for i in range(6)]
    results = calculate_results(marks)
    display_results(marks, results)


if __name__ == "__main__":
    main()