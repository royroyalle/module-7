from tkinter import *
from datetime import date

def calculate_age():
    user_name = name_entry.get()
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    
    result_text = f"Hello {user_name}! You are {age} years old."
    display_box.delete("1.0", END)
    display_box.insert(END, result_text)

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.config(bg="#F0F8FF")

Label(root, text="Name:", bg="#F0F8FF").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Day (DD):", bg="#F0F8FF").grid(row=1, column=0, padx=10, pady=10)
day_entry = Entry(root)
day_entry.grid(row=1, column=1)

Label(root, text="Month (MM):", bg="#F0F8FF").grid(row=2, column=0, padx=10, pady=10)
month_entry = Entry(root)
month_entry.grid(row=2, column=1)

Label(root, text="Year (YYYY):", bg="#F0F8FF").grid(row=3, column=0, padx=10, pady=10)
year_entry = Entry(root)
year_entry.grid(row=3, column=1)

calc_button = Button(root, text="Calculate Age", command=calculate_age, bg="#4682B4", fg="white")
calc_button.grid(row=4, column=0, columnspan=2, pady=20)

display_box = Text(root, height=2, width=40)
display_box.grid(row=5, column=0, columnspan=2, padx=10)

root.mainloop()