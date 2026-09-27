import sqlite3

conn = sqlite3.connect('college.db')

cursor = conn.cursor()

branch = 'AIE'

cursor.execute(
    'SELECT name, cgpa FROM students WHERE branch=?',
    (branch,)
)

for name,cgpa in cursor.fetchall():
    print(f"{name}: {cgpa}")