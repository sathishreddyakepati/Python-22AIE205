import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Update Arun's marks
cursor.execute("""
UPDATE students
SET marks = ?
WHERE id = ?
""", (95, 1))

connection.commit()

print("Student marks updated successfully!")

# Verify the update
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

connection.close()
