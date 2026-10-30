import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    marks INTEGER
)
""")
connection.commit()


def add_student():
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    department = input("Enter department: ")
    marks = int(input("Enter marks: "))

    cursor.execute("""
    INSERT INTO students (id, name, department, marks)
    VALUES (?, ?, ?, ?)
    """, (student_id, name, department, marks))

    connection.commit()
    print("Student added successfully.")


def display_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\nID   Name       Department   Marks")
    print("----------------------------------")

    for row in rows:
        print(row[0], row[1], row[2], row[3])


def update_marks():
    student_id = int(input("Enter student ID: "))
    marks = int(input("Enter new marks: "))

    cursor.execute("""
    UPDATE students
    SET marks = ?
    WHERE id = ?
    """, (marks, student_id))

    connection.commit()
    print("Marks updated successfully.")


def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    cursor.execute("""
    DELETE FROM students
    WHERE id = ?
    """, (student_id,))

    connection.commit()
    print("Student deleted successfully.")


while True:
    print("\n===== STUDENT DATABASE =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_marks()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

connection.close()
print("Database connection closed.")
