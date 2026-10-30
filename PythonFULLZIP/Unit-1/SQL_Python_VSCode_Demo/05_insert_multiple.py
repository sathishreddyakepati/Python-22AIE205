import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Insert more students
cursor.execute("""
INSERT INTO students (id, name, department, marks)
VALUES (?, ?, ?, ?)
""", (4, "Priya", "CSE", 91))

cursor.execute("""
INSERT INTO students (id, name, department, marks)
VALUES (?, ?, ?, ?)
""", (5, "Rahul", "ECE", 78))

connection.commit()

print("Two more students inserted successfully!")

connection.close()
