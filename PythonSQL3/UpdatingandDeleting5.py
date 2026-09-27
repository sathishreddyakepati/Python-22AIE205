import sqlite3

conn = sqlite3.connect('college.db')

cursor = conn.cursor()

cursor.execute('UPDATE students SET cgpa = ? WHERE roll_no =?',(9.0,102))

cursor.execute(
    'DELETE FROM students WHERE roll_no = ?',
    (104,)
)

conn.commit()

print("updated details")