import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Delete Rahul
cursor.execute("""
DELETE FROM students
WHERE id = ?
""", (3,))

connection.commit()

print("Student deleted successfully!")

# Verify the deletion
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

connection.close()
