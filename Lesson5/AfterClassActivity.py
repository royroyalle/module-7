import tkinter as tk

def check_strength(*args):
    password = password_entry.get()
    length = len(password)
    
    if length == 0:
        result_label.config(text="Enter a password", fg="black")
    elif length < 6:
        result_label.config(text="Strength: Weak", fg="red")
    elif length <= 10:
        result_label.config(text="Strength: Medium", fg="orange")
    else:
        result_label.config(text="Strength: Strong", fg="green")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

label = tk.Label(root, text="Enter Password:", font=("Arial", 10))
label.pack(pady=10)
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

password_entry.bind("<KeyRelease>", check_strength)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack(pady=20)

root.mainloop()