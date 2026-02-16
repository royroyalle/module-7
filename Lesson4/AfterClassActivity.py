import tkinter as tk
from tkinter import messagebox

def calculate_interests():
    try:
        p = float(entry_principal.get())
        r = float(entry_rate.get())
        t = float(entry_time.get())
        si = (p * r * t) / 100


        amount = p * (pow((1 + r / 100), t))
        ci = amount - p

        label_si_res.config(text=f"Simple Interest: {si:.2f}")
        label_ci_res.config(text=f"Compound Interest: {ci:.2f}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("300x350")
root.padx = 20


tk.Label(root, text="Principal Amount:").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time Period (Years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()


btn_calc = tk.Button(root, text="Calculate", command=calculate_interests, bg="#4CAF50", fg="white")
btn_calc.pack(pady=20)

label_si_res = tk.Label(root, text="Simple Interest: -", font=("Arial", 10, "bold"))
label_si_res.pack()

label_ci_res = tk.Label(root, text="Compound Interest: -", font=("Arial", 10, "bold"))
label_ci_res.pack()

root.mainloop()