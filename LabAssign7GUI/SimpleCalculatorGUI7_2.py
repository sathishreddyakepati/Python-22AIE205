import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("350x450")

display = tk.Entry(
    window,
    font=("Arial", 20),
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def button_click(value):
    display.insert(tk.END, value)
def clear():
    display.delete(0, tk.END)
def calculate():
    expression = display.get()
    try:
        result = eval(expression)#for evaluating math expression string
        display.delete(0, tk.END)
        display.insert(0, result)

    except ZeroDivisionError:
        messagebox.showerror(
            "Error",
            "Cannot divide by zero"
        )
        clear()
    except:
        messagebox.showerror(
            "Error",
            "Invalid operation"
        )
        clear()

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),

    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),

    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),

    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 2),
    ("=", 4, 3)
]

for text, row, column in buttons:
    if text == "=":
        button = tk.Button(
            window,
            text=text,
            width=7,
            height=2,
            command=calculate
        )
    else:
        button = tk.Button(
            window,
            text=text,
            width=7,
            height=2,
            command=lambda value=text: button_click(value)
            #when this button is clciked ,send its text to button_click()
        )
    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )
clear_button = tk.Button(
    window,
    text="Clear",
    width=31,
    height=2,
    command=clear
)
clear_button.grid(
    row=5,
    column=0,
    columnspan=4,
    padx=5,
    pady=10
)
window.mainloop()