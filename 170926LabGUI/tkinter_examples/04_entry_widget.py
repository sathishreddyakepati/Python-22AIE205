"""
Demo 4: Entry Widget
----------------------
Concept: An Entry allows the user to type a single line of text.
"""

import tkinter as tk

window = tk.Tk()
window.title("Entry Demo")
window.geometry("400x200")

label = tk.Label(window, text="Enter your name:")
label.pack(pady=(30, 5))

name_entry = tk.Entry(window)
name_entry.pack()

window.mainloop()
