import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

print("Database connected!")
print("Cursor created!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    marks INTEGER
)
""")

connection.commit()

print("Students table created successfully!")

connection.close()
