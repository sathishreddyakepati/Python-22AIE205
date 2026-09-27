import tkinter as tk

window = tk.Tk()
window.geometry("400x300")

def printHello():
    print("Hello")

button = tk.Button(
    window,
    text="Click here!",
    command=printHello
)
button.pack()

window.mainloop()