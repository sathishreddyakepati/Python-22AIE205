import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("My Application")
window.geometry("400x300")

label1 = tk.Label(window,
                  text="Enter Name")
label1.pack()

entry = tk.Entry(window)
entry.pack()

def function():
    name = entry.get()
    if name=="":
        messagebox.showwarning("Warning", "Invalid input!")
    label1.config(text="hELLO "+name)

btn = tk.Button(window, text="Submit",command=function)
btn.pack()



window.mainloop()