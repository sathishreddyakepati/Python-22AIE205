import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("Student Records:")
print("----------------")

for row in rows:
    print(row)

connection.close()
