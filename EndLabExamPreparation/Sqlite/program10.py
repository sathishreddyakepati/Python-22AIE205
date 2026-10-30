import sqlite3

conn = sqlite3.Connection("student.db")
cursor = conn.cursor()

#create student table

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    marks INTEGER
    )""")

conn.commit()

# add student function

def add_student():
    student_id = int(ino)