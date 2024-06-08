"""
Problem Statement:
You have a list of daily temperatures for a month, and you'd like to extract specific data from it.
"""
# Task 1: Given the list of temperatures:
#Extract the temperatures for the second week (7 days) of the month. Expected Outcome: 83, 85, 86, 87, 88, 89, 90


temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]


week_2 = temperatures[7:14]
print(week_2)

# Task 2: Extract all the temperatures above 100.

above_100 = temperatures[24:30]
print(above_100)

#Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures.sort()
temperatures.reverse()
print(temperatures)
print(temperatures[4:10])

