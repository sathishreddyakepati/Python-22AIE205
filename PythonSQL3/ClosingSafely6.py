import sqlite3

try:
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM students')
    print('Total students in db:',cursor.fetchone()[0])

except sqlite3.Error as e:
    print('Database error: ', e)

finally:
    conn.close()

    