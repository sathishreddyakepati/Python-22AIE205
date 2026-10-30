import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Insert one student
cursor.execute("""
INSERT INTO students (id, name, department, marks)
VALUES (?, ?, ?, ?)
""", (3, "Don", "CSE-CYS", 75))

connection.commit()

print("Student inserted successfully!")

connection.close()
