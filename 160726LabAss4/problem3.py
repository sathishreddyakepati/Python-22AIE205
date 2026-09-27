register_numbers = []
student_names = []
departments = []

student_records = {}
department_students = {}
elective_count = {}

Nstudents = int(input("Enter no.of students: "))

i = 1

while Nstudents >= 1:

    print("Student", i)

    reg = input("Enter Register Number: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")

    register_numbers.append(reg)
    student_names.append(name)
    departments.append(dept)

    identity = (reg, name, dept)

    n = int(input("Enter no.of electives: "))

    electives = set()

    item = 1

    while n >= 1:

        course = input("Enter Elective " + str(item) + ": ")

        electives.add(course)

        if course in elective_count:
            elective_count[course] += 1
        else:
            elective_count[course] = 1

        item += 1
        n -= 1

    student_records[reg] = {
        "Identity": identity,
        "Electives": electives
    }

    if dept not in department_students:
        department_students[dept] = []
        department_students[dept] = []

    department_students[dept].append(reg)

    i += 1
    Nstudents -= 1

most_popular = ""
least_popular = ""

maximum = -1
minimum = 1000

for course in elective_count:

    if elective_count[course] > maximum:
        maximum = elective_count[course]
        most_popular = course

    if elective_count[course] < minimum:
        minimum = elective_count[course]
        least_popular = course

print("\nMost Popular Elective :", most_popular)
print("Least Popular Elective :", least_popular)

print("\nStudents choosing more than three electives")

for reg in student_records:

    if len(student_records[reg]["Electives"]) > 3:
        print(student_records[reg]["Identity"][1])

same_courses = []

regs = list(student_records.keys())

i = 0

while i < len(regs):
    j = i + 1
    while j < len(regs):
        if student_records[regs[i]]["Electives"] == student_records[regs[j]]["Electives"]:
            same_courses.append((regs[i], regs[j]))
        j += 1
    i += 1
    print("\nStudents with Identical Elective Combinations")

if len(same_courses) == 0:
    print("None")
else:
    i = 0
    while i < len(same_courses):
        print(student_records[same_courses[i][0]]["Identity"][1],
              "and",
              student_records[same_courses[i][1]]["Identity"][1])
        i += 1

print("\nElectives Selected by Only One Student")

for course in elective_count:

    if elective_count[course] == 1:
        print(course)

print("\nDepartment-wise Enrollment Statistics")

for dept in sorted(department_students):

    print(dept, ":", len(department_students[dept]), "Students")

print("\nRecommended Electives")

for reg in student_records:

    dept = student_records[reg]["Identity"][2]

    recommend = ""

    for student in department_students[dept]:

        if student != reg:

            for course in student_records[student]["Electives"]:

                if course not in student_records[reg]["Electives"]:

                    recommend = course
                    break

        if recommend != "":
            break

    if recommend == "":
        print(student_records[reg]["Identity"][1], "-> No Recommendation")
    else:
        print(student_records[reg]["Identity"][1], "->", recommend)

print("\nAll Reports in Sorted Order")

print("\nDepartments")

for dept in sorted(department_students):
    print(dept)

print("\nElectives")

for course in sorted(elective_count):
    print(course)

print("\nStudents")

for reg in sorted(student_records):

    print(student_records[reg]["Identity"][1])

print("\nEnd of Report")