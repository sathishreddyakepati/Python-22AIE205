"""
Demo 8: Layout Management - pack()
--------------------------------------
Concept: pack() is the simplest layout manager. It stacks widgets
         one after another (top-to-bottom by default).
"""

import tkinter as tk

window = tk.Tk()
window.title("pack() Demo")
window.geometry("300x200")

tk.Label(window, text="Widget 1").pack()
tk.Label(window, text="Widget 2").pack()
tk.Button(window, text="Widget 3 (Button)").pack()

window.mainloop()
