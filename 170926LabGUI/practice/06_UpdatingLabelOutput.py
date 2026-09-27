import tkinter as tk

window = tk.Tk()
window.geometry("400x300")

label = tk.Label(
    window,
    text = "Please Enter your name",
    font=("Arial",16)
)
label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

# .config() changes label properties
def show_name():
    name = name_entry.get()
    label.config(text="Hello " + name)


button = tk.Button(
    window,
    text = "Enter",
    command=show_name
)
button.pack()

window.mainloop()