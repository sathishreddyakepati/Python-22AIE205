"""
Demo 2: Label Widget
---------------------
Concept: A Label displays text or information on the window.
"""

import tkinter as tk

window = tk.Tk()
window.title("Label Demo")
window.geometry("600x400")

label = tk.Label(window, text="Welcome to Python GUI", font=("Arial", 14))
label.pack(pady=60)

window.mainloop()
