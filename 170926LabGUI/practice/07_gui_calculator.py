import tkinter as tk


def add_numbers():
    a = float(num1.get())
    b = float(num2.get())
    result = a + b
    result_label.config(text="Result: " + str(result))


window = tk.Tk()
window.title("Addition Calculator")
window.geometry("300x250")

tk.Label(window, text="First Number").pack(pady=(20, 0))
num1 = tk.Entry(window)
num1.pack()

tk.Label(window, text="Second Number").pack(pady=(10, 0))
num2 = tk.Entry(window)
num2.pack()

tk.Button(window, text="Add", command=add_numbers).pack(pady=15)

result_label = tk.Label(window, text="Result:", font=("Arial", 12))
result_label.pack()

window.mainloop()
