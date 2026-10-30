import sqlite3

connection = sqlite3.connect("college.db")

print("Database connected successfully!")

connection.close()
print("Database connection closed!")
