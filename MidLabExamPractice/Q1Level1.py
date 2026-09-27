# Q1. Student Marks Analyzer

# Write a Python program that accepts marks of 5 subjects in a list and:

# Calculate total and average.
# Find highest and lowest marks.
# Count how many subjects are passed (>= 40).
# Display Pass if all subjects are passed, otherwise Fail.

marks = []

for i in range(0,5):
    m = int(input(f"Enter marks of Subject {i+1}: "))
    marks.insert(i,m)

total = sum(marks)
average = total/len(marks)

highest = max(marks)
lowest = min(marks)

print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")
print(f"Total: {total}")
print(f"Average: {average}")
count = 0

for i in range(0,len(marks)):
    if marks[i]>=40:
        count+=1
print(f"Passed count: {count}")
if(count==len(marks)):
    print("passed")
else:
    print("Fail")