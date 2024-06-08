#Task 1: Given the two lists:
#Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted.sort()
attended.sort()

print(submitted)
print(attended)

#Task 2: Check if the two lists are identical in terms of their content, regardless of order.

if "Alice" in submitted and "Alice" in attended:
    print("Alice both submitted the assignment and attended class")
else:
    print("Alice: Both tasks not complete.")

if "Bob" in submitted and "Bob" in attended:
    print("Bob: Both submitted the assignment and attended class")
else:
    print("Bob: Both tasks not complete.")
    
if "Charlie" in submitted and "Charlie" in attended:
    print("Charlie: Both submitted the assignment and attended class")
else:
    print("Charlie: Both tasks not complete.")

if "David" in submitted and "David" in attended:
    print("David: both submitted the assignment and attended class")
else:
    print("David: Both tasks not complete.")
    
if "Eve" in submitted and "Eve" in attended:
    print("Eve: both tasks not complete.")
else:
    print("Eve: both tasks not complete.")
    
if "Frank" in submitted and "Frank" in attended:
    print("Frank: Both submitted the assignment and attended class")
else:
    print("Frank: Both tasks not complete.")
    
    
#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
attended.remove("Eve")
attended.remove("Frank")
print(attended)


