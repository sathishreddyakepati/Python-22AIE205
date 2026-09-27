import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
#label creation
label = tk.Label(
    window,
    text="First Label Text",
    font=("Arial",16)
)
#pack used to put

label.pack()

window.mainloop()