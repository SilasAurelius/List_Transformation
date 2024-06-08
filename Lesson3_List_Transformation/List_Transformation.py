"""
Problem Statement:
You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.
"""

#Task 1: Given the list of grades:
#Sort the grades in descending order and display the sorted list.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
print(grades)

grades.reverse()
print(grades)
#Task 2: Calculate the average grade and display it.

average_grade = sum(grades) / len(grades)
print(f"The average grade is: {average_grade}")

#Task 3: Replace any grade below 80 with the value Failed.

grades[7] = "Failed"
grades[8] = "Failed"
grades[9] = "Failed"
print(grades)