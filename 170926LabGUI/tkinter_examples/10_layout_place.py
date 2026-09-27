"""
Demo 10: Layout Management - place()
----------------------------------------
Concept: place() positions widgets using exact x, y coordinates.
         Gives precise control but is less flexible for beginners.
"""

import tkinter as tk

window = tk.Tk()
window.title("place() Demo")
window.geometry("300x200")

tk.Label(window, text="Positioned Label").place(x=50, y=150)
tk.Button(window, text="Positioned Button").place(x=100, y=150)

window.mainloop()
