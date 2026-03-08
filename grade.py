# Student Grade Calculator

# Get student's name
name = input("Enter student's name: ")

# Get 3 subject marks
mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Determine Pass or Fail
if average >= 40:
    result = "Pass"
else:
    result = "Fail"

# Display results
print(f"\nStudent Name: {name}")
print(f"Subject 1: {mark1}")
print(f"Subject 2: {mark2}")
print(f"Subject 3: {mark3}")
print(f"Average: {average:.2f}")
print(f"Result: {result}")
