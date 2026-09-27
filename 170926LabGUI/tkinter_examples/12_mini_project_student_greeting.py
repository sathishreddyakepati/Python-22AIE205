"""
Demo 12: Mini Project - Student Greeting App
-------------------------------------------------
Concept: Combines everything taught so far -
         Window -> Label -> Entry -> Button -> Function ->
         Input -> Validation -> Output -> Message Box
"""

import tkinter as tk
from tkinter import messagebox


def greet_student():
    name = name_entry.get()
    if name == "":
        messagebox.showwarning("Warning", "Please enter your name")
    else:
        result.config(text="Welcome, " + name + "!")


window = tk.Tk()
window.title("Student Greeting App")
window.geometry("400x250")

title = tk.Label(window, text="Student Greeting App", font=("Arial", 14, "bold"))
title.pack(pady=20)

tk.Label(window, text="Enter your name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Button(window, text="Greet", command=greet_student).pack(pady=15)

result = tk.Label(window, text="", font=("Arial", 12))
result.pack()

window.mainloop()
