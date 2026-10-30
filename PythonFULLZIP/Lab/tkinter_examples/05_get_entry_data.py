"""
Demo 5: Getting Data from Entry
----------------------------------
Concept: The get() method retrieves the value typed by the user.
Flow: User enters "Prabu" -> name_entry.get() -> name = "Prabu"
      -> print("Hello Prabu")
"""

import tkinter as tk


def show_name():
    name = name_entry.get()
    print("Hello", name)


window = tk.Tk()
window.title("Get Entry Data Demo")
window.geometry("400x200")

name_entry = tk.Entry(window)
name_entry.pack(pady=(30, 10))

button = tk.Button(window, text="Submit", command=show_name)
button.pack()

window.mainloop()
