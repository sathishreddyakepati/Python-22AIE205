import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Income Tax Calculator")
window.geometry("400x500")

label1 = tk.Label(window, text="Enter Annual Income:")
label1.pack(pady=(10, 5))

annualIncome = tk.Entry(window)
annualIncome.pack()

regime_label = tk.Label(window, text="Select Tax Regime:")
regime_label.pack(pady=(15, 5))

regime = tk.StringVar()
regime.set("New Regime")
#radio buttons
old_regime = tk.Radiobutton(
    window,
    text="Old Regime",
    variable=regime,
    value="Old Regime"
)
old_regime.pack()

new_regime = tk.Radiobutton(
    window,
    text="New Regime",
    variable=regime,
    value="New Regime"
)
new_regime.pack()

def calculate_tax():
    try:
        income = int(annualIncome.get())
        if income < 0:
            messagebox.showwarning(
                "Invalid Input",
                "Income cannot be negative"
            )
            return
        selected_regime = regime.get()
        if selected_regime == "New Regime":
            if income <= 400000:
                taxAmount = 0
            elif income <= 800000:
                taxableAmount = income - 400000
                taxAmount = taxableAmount * 0.05
            elif income <= 1200000:
                taxableAmount = income - 400000
                taxAmount = (taxableAmount - 400000) * 0.10 + 400000 * 0.05
            elif income <= 1600000:
                taxableAmount = income - 400000
                taxAmount = (
                    400000 * 0.05
                    + 400000 * 0.10
                    + (taxableAmount - 800000) * 0.15
                )
            else:
                taxableAmount = income - 400000
                taxAmount = (
                    400000 * 0.05
                    + 400000 * 0.10
                    + 400000 * 0.15
                    + (taxableAmount - 1200000) * 0.20
                )
        else:
            if income <= 250000:
                taxAmount = 0
            elif income <= 500000:
                taxableAmount = income - 250000
                taxAmount = taxableAmount * 0.05
            elif income <= 1000000:
                taxableAmount = income - 250000
                taxAmount = (
                    250000 * 0.05
                    + (taxableAmount - 250000) * 0.20
                )
            else:
                taxableAmount = income - 250000
                taxAmount = (
                    250000 * 0.05
                    + 500000 * 0.20
                    + (taxableAmount - 750000) * 0.30
                )

        result_label.config(
            text="Result:\nIncome Tax: ₹" + str(round(taxAmount, 2))
            +"\n Annual Income: "+annualIncome.get()
            +"\nRegime selected : "+selected_regime
        )
    except ValueError:
        messagebox.showwarning(
            "Invalid Input",
            "Please enter a valid annual income"
        )
calculate_button = tk.Button(
    window,
    text="Calculate Tax",
    command=calculate_tax
)
calculate_button.pack(pady=20)
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=10)
def reset():
    annualIncome.delete(0, tk.END)
    regime.set("New Regime")
    result_label.config(text="Income Tax:")
reset_button = tk.Button(
    window,
    text="Reset",
    command=reset
)
reset_button.pack(pady=10)

window.mainloop()