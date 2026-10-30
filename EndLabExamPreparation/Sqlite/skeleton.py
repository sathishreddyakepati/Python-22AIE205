import sqlite3

Connection = sqlite3.connect("college.db")
cursor = Connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    marks INTEGER
    ) 
""")

Connection.commit()

cursor.execute("""
INSERT INTO students (id, name, department, marks)
VALUES(?, ?, ?, ?)
""",(2,"dOnn","AIE", 75))
Connection.commit()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

Connection.close()