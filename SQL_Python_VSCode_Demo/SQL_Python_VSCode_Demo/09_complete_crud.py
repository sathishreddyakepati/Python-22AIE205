import sqlite3

# CONNECT
connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    marks INTEGER
)
""")
connection.commit()

# INSERT
cursor.execute("""
INSERT INTO students (id, name, department, marks)
VALUES (?, ?, ?, ?)
""", (10, "Kumar", "CSE", 88))
connection.commit()

print("INSERT completed.")

# SELECT
cursor.execute("SELECT * FROM students")
print("\nAfter INSERT:")
for row in cursor.fetchall():
    print(row)

# UPDATE
cursor.execute("""
UPDATE students
SET marks = ?
WHERE id = ?
""", (94, 10))
connection.commit()

print("\nAfter UPDATE:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# DELETE
cursor.execute("""
DELETE FROM students
WHERE id = ?
""", (10,))
connection.commit()

print("\nAfter DELETE:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# CLOSE
connection.close()
print("\nDatabase connection closed.")
