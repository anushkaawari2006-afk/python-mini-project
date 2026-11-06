"""
grade_calculator.py - Student Grade Calculator
Module 02: Python Mini Project

A command-line program that:
  - takes a student's name and marks for any number of subjects
  - calculates total, percentage, grade and pass/fail result
  - shows the highest and lowest scoring subjects
  - supports multiple students and prints a class summary at the end
"""

PASS_PERCENTAGE = 40      # minimum overall percentage to pass
PASS_SUBJECT_MARKS = 35   # minimum marks needed in every subject
MAX_MARKS = 100           # maximum marks per subject


def get_int(prompt, minimum, maximum):
    """Keep asking until the user enters a whole number in the given range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"  Please enter a number between {minimum} and {maximum}.")


def get_name(prompt):
    """Keep asking until the user types a non-empty name."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("  This field cannot be empty.")


def calculate_grade(percentage):
    """Return a letter grade for the given percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    return "F"


def read_student():
    """Ask for a student's details and return them as a dictionary."""
    name = get_name("\nEnter student name: ")
    count = get_int("Number of subjects (1-10): ", 1, 10)

    subjects = {}  # subject name -> marks
    for i in range(1, count + 1):
        subject = get_name(f"  Subject {i} name: ")
        marks = get_int(f"  Marks in {subject} (0-{MAX_MARKS}): ", 0, MAX_MARKS)
        subjects[subject] = marks

    total = sum(subjects.values())
    maximum = count * MAX_MARKS
    percentage = total / maximum * 100
    passed = percentage >= PASS_PERCENTAGE and all(
        m >= PASS_SUBJECT_MARKS for m in subjects.values()
    )

    return {
        "name": name,
        "subjects": subjects,
        "total": total,
        "maximum": maximum,
        "percentage": percentage,
        "grade": calculate_grade(percentage),
        "passed": passed,
    }


def print_report(student):
    """Print a formatted report card for one student."""
    print("\n" + "=" * 40)
    print(f"REPORT CARD: {student['name']}")
    print("=" * 40)
    for subject, marks in student["subjects"].items():
        print(f"{subject:<20} {marks:>5} / {MAX_MARKS}")
    print("-" * 40)
    print(f"{'Total':<20} {student['total']:>5} / {student['maximum']}")
    print(f"{'Percentage':<20} {student['percentage']:>5.2f} %")
    print(f"{'Grade':<20} {student['grade']:>5}")
    print(f"{'Result':<20} {'PASS' if student['passed'] else 'FAIL':>5}")

    best = max(student["subjects"], key=student["subjects"].get)
    worst = min(student["subjects"], key=student["subjects"].get)
    print("-" * 40)
    print(f"Strongest subject: {best} ({student['subjects'][best]})")
    print(f"Weakest subject:   {worst} ({student['subjects'][worst]})")
    print("=" * 40)


def print_class_summary(students):
    """Print a summary of all students entered in this session."""
    print("\n" + "#" * 40)
    print("CLASS SUMMARY")
    print("#" * 40)
    print(f"{'Name':<15} {'Percent':>8} {'Grade':>6} {'Result':>7}")
    for s in students:
        result = "PASS" if s["passed"] else "FAIL"
        print(f"{s['name']:<15} {s['percentage']:>7.2f}% {s['grade']:>6} {result:>7}")

    average = sum(s["percentage"] for s in students) / len(students)
    topper = max(students, key=lambda s: s["percentage"])
    passed = sum(1 for s in students if s["passed"])
    print("-" * 40)
    print(f"Students: {len(students)} | Passed: {passed} | Failed: {len(students) - passed}")
    print(f"Class average: {average:.2f}%")
    print(f"Topper: {topper['name']} ({topper['percentage']:.2f}%)")


def main():
    print("=== Student Grade Calculator ===")
    students = []

    while True:
        student = read_student()
        print_report(student)
        students.append(student)

        again = input("\nAdd another student? (y/n): ").strip().lower()
        if again != "y":
            break

    print_class_summary(students)
    print("\nThank you for using the Grade Calculator!")


if __name__ == "__main__":
    main()
