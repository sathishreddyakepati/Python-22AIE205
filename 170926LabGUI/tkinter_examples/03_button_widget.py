"""
Demo 3: Button Widget
-----------------------
Concept: A Button performs an action when the user clicks it.
Flow: User clicks button -> command=say_hello -> say_hello() runs.

Note: command=say_hello  (no parentheses)
      command=say_hello() would call the function immediately - wrong!
"""

import tkinter as tk


def say_hello():
    print("Hello!")


window = tk.Tk()
window.title("Button Demo")
window.geometry("800x600")

button = tk.Button(window, text="Click Me", command=say_hello)
button.pack(pady=30)

window.mainloop()
