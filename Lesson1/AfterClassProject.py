from tkinter import *

def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    
    result_box.delete("1.0", END)
    result_box.insert(END, product)

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

label_desc = Label(root, text="This application calculates the product of two numbers.")
label_desc.pack(pady=10)

label1 = Label(root, text="Enter first number:")
label1.pack()
entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Enter second number:")
label2.pack()
entry2 = Entry(root)
entry2.pack()

calc_button = Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=15)

label_res = Label(root, text="Result:")
label_res.pack()
result_box = Text(root, height=1, width=20)
result_box.pack()

root.mainloop()