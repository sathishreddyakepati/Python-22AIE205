import sqlite3

conn = sqlite3.connect('college.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
roll_no INTEGER PRIMARY KEY,
name TEXT NOT NULL,
branch TEXT,
cgpa REAL)'''
)

conn.commit()
print('Table has created successfully')
