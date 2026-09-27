# Write a Python program for a university that accepts information for N students.

# For each student, collect:

# Register number
# Name
# Department
# Marks in 5 subjects
# # ----Requirements---
# Store each student's information in a dictionary.
# Store the 5 marks in a list.
# Calculate:
# Total marks
# Average marks
# Grade
# Find the overall topper.
# Find the class average.
# Display students who scored above 90 in at least 3 subjects.
# Display all student records.

students = []
n = int(input("Enter no.of students: "))
for i in range(0,n):
    reg = input(f"Enter register number of student{i+1}: ")
    Name = input(f"Enter Name of student{i+1}: ")
    Depart = input(f"Enter Department of student{i+1}: ")

    marks = []
    total = 0
    above90 = 0
    for j in range(0,5):
        m = int(input(f"Enter marks of subject {j+1}: "))
        if m>90:
            above90+=1
        total+=m
        marks.append(m)
    avg = total/5
    if avg>=90:
        g = 'A'
    elif avg>=80:
        g='B'
    elif avg>=70:
        g='C'
    elif avg>=60:
        g='D'
    elif avg<60:
        g='F'

    dict = {
        "reg":reg,
         "Name":Name,
         "Department":Depart,
         "marks": marks,
         "Total":total,
         "Average":avg,
         "Grade":g,
         "Above90":above90,
    }

    students.append(dict)
#class average
classTotal = 0
for student in students:
    classTotal+=student["Total"]

classAverage = classTotal/len(students) 
#overall Topper
top = 0
topMarks = 0
for i in range(0,len(students)):
    if students[i]["Total"] > students[top]["Total"]:
        top = i
        topMarks = students[i]["Total"]
 #above90 students

A90 = []

for student in students:
    if(student["Above90"]>=3):
        A90.append(student["Name"])

print("------------Student Records---------------")
for student in students:
    # print(student.items().to_string())
    print(student)
print("Class Average : ",classAverage)
print("Class overall topper is Student ",students[top]["Name"])
print("Students with 3+ marks above 90: ",A90)



