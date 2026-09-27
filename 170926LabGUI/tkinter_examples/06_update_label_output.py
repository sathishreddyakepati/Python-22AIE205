"""
Demo 6: Displaying the Result in the GUI
--------------------------------------------
Concept: Instead of printing to the terminal, update a Label's text
         using result_label.config(text=...).
"""

import tkinter as tk


def show_name():
    name = name_entry.get()
    result_label.config(text="Hello " + name)


window = tk.Tk()
window.title("Update Label Demo")
window.geometry("400x220")

name_entry = tk.Entry(window)
name_entry.pack(pady=(30, 10))

button = tk.Button(window, text="Submit", command=show_name)
button.pack()

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=30)

window.mainloop()
