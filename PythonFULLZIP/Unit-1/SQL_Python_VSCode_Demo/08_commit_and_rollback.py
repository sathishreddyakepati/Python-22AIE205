import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Change Arun's marks temporarily
cursor.execute("""
UPDATE students
SET marks = ?
WHERE id = ?
""", (100, 1))

print("Temporary change made.")

# Cancel the change
connection.rollback()

print("Changes rolled back.")

# Check the database
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

connection.close()
