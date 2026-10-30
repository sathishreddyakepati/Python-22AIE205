import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        p = int(python_marks.get())
        j = int(java_marks.get())
        c = int(CN_marks.get())
        total = p+j+c
        average = total/3
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"
    except ValueError:
        messagebox.showwarning("Warning","marks cannot be empty!")
    else:
        label5.config(text="Student :"+name.get()+"\nTotal :"+str(total)+"\nAverage: "+str(average)+"\n Grade: "+grade)


window = tk.Tk()
window.title("Student Result Calculator")
window.geometry("500x400")
label1 = tk.Label(window, text="Name:")
label1.grid(row=0,column=0)

name = tk.Entry(window)
name.grid(row=0,column=1)

label2 = tk.Label(window, text="Python marks: ")
label2.grid(row=1,column=0)
python_marks = tk.Entry(window)
python_marks.grid(row=1,column=1)


label3 = tk.Label(window, text="Java marks: ")
label3.grid(row=2,column=0)
java_marks = tk.Entry(window)
java_marks.grid(row=2,column=1)


label4 = tk.Label(window, text="CN marks: ")
label4.grid(row=3,column=0)
CN_marks = tk.Entry(window)
CN_marks.grid(row=3,column=1)

btn = tk.Button(window, text="Calculate", command=calculate)
btn.grid(row=4,column=0)
label5 = tk.Label(window, text="Click above button to calculate!")
label5.grid(row=5,column=0, columnspan=2)

window.mainloop()