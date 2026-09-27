import sqlite3
conn = sqlite3.connect('college.db')
cursor = conn.cursor()
cursor.execute(
    'INSERT INTO students VALUES (?, ?, ?, ?)',
    (101, 'Sathish', 'AIE', 9.0)
)

students_datarecord = [
    (102, 'Akhil', 'AIE', 8.1),
    (103, 'Akhila', 'CSE', 7.5),
    (104, 'Akhilesh', 'AIDS', 8.9)
]

cursor.executemany(
    'INSERT INTO students VALUES (?, ?, ?, ?)',
    students_datarecord
)

conn.commit()
print("Students Data inserted successfully")


