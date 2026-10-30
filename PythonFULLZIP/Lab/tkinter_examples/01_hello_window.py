"""
Demo 1: Creating a Simple Window
---------------------------------
Concept: window = tk.Tk() creates the main window.
          window.title() / window.geometry() configure it.
          window.mainloop() starts the GUI event loop and keeps
          the window open, waiting for user actions.
"""

import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.geometry("400x300")

window.mainloop()
