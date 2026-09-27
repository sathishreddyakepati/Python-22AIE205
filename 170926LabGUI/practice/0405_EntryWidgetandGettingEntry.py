import tkinter as tk

window = tk.Tk()
window.geometry("400x300")

name_Entry = tk.Entry(window)
name_Entry.pack()
# name_Entry.get()
def show_name():
    name = name_Entry.get()
    print("Hello", name)

button = tk.Button(
    window,
    text="Enter",
    command=show_name)
button.pack()
window.mainloop()