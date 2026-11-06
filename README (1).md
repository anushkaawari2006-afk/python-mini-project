# Student Grade Calculator

**Module 02: Python Mini Project (Day 5 – Day 8, Beginner)**

A command-line Python program that calculates a student's total marks, percentage, grade and pass/fail result, then shows a class summary for all students entered.

## Features
- Enter any number of students and 1 to 10 subjects each
- Input validation: rejects text, empty names and marks outside 0 to 100
- Calculates total, percentage and letter grade (A+ to F)
- Pass/fail rule: at least 40% overall and at least 35 marks in every subject
- Shows each student's strongest and weakest subject
- Class summary with average, topper and pass/fail count

## Grading Scale

| Percentage | Grade |
|-----------|-------|
| 90 and above | A+ |
| 80 – 89 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| 50 – 59 | D |
| 40 – 49 | E |
| Below 40 | F |

## Python Concepts Used
- Variables and data types
- `if / elif / else` conditions
- `for` and `while` loops
- Functions with parameters and return values
- Lists and dictionaries
- Exception handling (`try / except`)
- `max`, `min`, `sum`, `all` and `lambda`

## How to Run

Requires Python 3.

```bash
python grade_calculator.py
```

## Sample Run

```
=== Student Grade Calculator ===

Enter student name: Asha
Number of subjects (1-10): 3
  Subject 1 name: Maths
  Marks in Maths (0-100): 90
  Subject 2 name: Science
  Marks in Science (0-100): 85
  Subject 3 name: English
  Marks in English (0-100): 78

========================================
REPORT CARD: Asha
========================================
Maths                   90 / 100
Science                 85 / 100
English                 78 / 100
----------------------------------------
Total                  253 / 300
Percentage           84.33 %
Grade                    A
Result                PASS
----------------------------------------
Strongest subject: Maths (90)
Weakest subject:   English (78)
========================================
```

## Possible Improvements
- Save results to a CSV file
- Add a graphical interface with Tkinter
- Show a bar chart of marks using matplotlib

## Author
Your Name Here
