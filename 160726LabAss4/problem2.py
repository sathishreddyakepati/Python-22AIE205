student_records = {}
department_students = {}
subject_totals = [0, 0, 0, 0, 0]

n = int(input("Enter number of students: "))

for i in range(n):

    print("\nStudent", i + 1)

    reg_no = input("Enter Register Number: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")

    identity = (reg_no, name, department)

    marks = []
    total = 0
    pass_count = 0
    above90 = 0

    print("Enter marks of 5 subjects")

    for j in range(5):

        mark = int(input("Subject " + str(j + 1) + ": "))

        marks.append(mark)

        total += mark

        subject_totals[j] += mark

        if mark >= 50:
            pass_count += 1

        if mark > 90:
            above90 += 1

    average = total / 5

    percentage = average

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 50:
        grade = "E"
    else:
        grade = "F"

    if pass_count == 5:
        status = "Pass"
    else:
        status = "Fail"

    student_records[reg_no] = {
        "Identity": identity,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Percentage": percentage,
        "Grade": grade,
        "Status": status,
        "Above90": above90,
        "FailSubjects": 5 - pass_count
    }

    if department not in department_students:
        department_students[department] = set()

    department_students[department].add(reg_no)

overall_topper = ""
highest_total = -1

department_toppers = {}

for reg_no in student_records:

    student = student_records[reg_no]

    if student["Total"] > highest_total:
        highest_total = student["Total"]
        overall_topper = student

    dept = student["Identity"][2]

    if dept not in department_toppers:
        department_toppers[dept] = student

    elif student["Total"] > department_toppers[dept]["Total"]:
        department_toppers[dept] = student

print("\nOverall Topper :", overall_topper["Identity"][1])
print("\nDepartment-wise Toppers")

for dept in department_toppers:
    print(dept, ":", department_toppers[dept]["Identity"][1])

print("\nStudents scoring above 90 in at least three subjects")

for reg_no in student_records:
    if student_records[reg_no]["Above90"] >= 3:
        print(student_records[reg_no]["Identity"][1])

print("\nStudents failing in exactly one subject")

for reg_no in student_records:
    if student_records[reg_no]["FailSubjects"] == 1:
        print(student_records[reg_no]["Identity"][1])

highest_average = subject_totals[0] / n
subject = 1

for i in range(1, 5):

    average = subject_totals[i] / n

    if average > highest_average:
        highest_average = average
        subject = i + 1

print("\nSubject with Highest Class Average : Subject", subject)

department_report = {}

for dept in department_students:

    department_report[dept] = {
        "Students": 0,
        "Pass": 0,
        "TotalMarks": 0,
        "Highest": -1,
        "Lowest": 501
    }
    names = {}

for reg_no in student_records:

    student = student_records[reg_no]

    dept = student["Identity"][2]

    department_report[dept]["Students"] += 1
    department_report[dept]["TotalMarks"] += student["Total"]

    if student["Status"] == "Pass":
        department_report[dept]["Pass"] += 1
    if student["Total"] > department_report[dept]["Highest"]:
        department_report[dept]["Highest"] = student["Total"]
    if student["Total"] < department_report[dept]["Lowest"]:
        department_report[dept]["Lowest"] = student["Total"]
    name = student["Identity"][1]
    if name not in names:
        names[name] = set()
    names[name].add(dept)

print("\nDuplicate Student Names Across Departments")

for name in names:
    if len(names[name]) > 1:
        print(name)

print("\nDepartment-wise Report")

for dept in department_report:

    students = department_report[dept]["Students"]

    pass_percentage = (department_report[dept]["Pass"] / students) * 100

    average_marks = department_report[dept]["TotalMarks"] / students

    print("\nDepartment :", dept)
    print("Number of Students :", students)
    print("Pass Percentage :", pass_percentage)
    print("Average Marks :", average_marks)
    print("Highest Scorer :", department_report[dept]["Highest"])
    print("Lowest Scorer :", department_report[dept]["Lowest"])