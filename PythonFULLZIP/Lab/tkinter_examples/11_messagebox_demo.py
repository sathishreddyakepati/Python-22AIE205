"""
Demo 11: Message Box
------------------------
Concept: Tkinter can display popup messages using the messagebox module.
"""

import tkinter as tk
from tkinter import messagebox


def show_message():
    messagebox.showinfo("Message", "Welcome to Python!")


window = tk.Tk()
window.title("Message Box Demo")
window.geometry("300x150")

button = tk.Button(window, text="Click Me", command=show_message)
button.pack(pady=50)

window.mainloop()
