"""
Demo 9: Layout Management - grid()
--------------------------------------
Concept: grid() arranges widgets in rows and columns - useful for
         form-style layouts (label + input side by side).
"""

import tkinter as tk

window = tk.Tk()
window.title("grid() Demo")
window.geometry("300x150")

tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(window).grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Age:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(window).grid(row=1, column=1, padx=10, pady=10)

tk.Button(window, text="Submit").grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
