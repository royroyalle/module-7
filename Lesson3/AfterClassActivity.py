from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("Length Converter App")

def f1():
    e2.delete(0, END)
    try:
        val = float(e1.get())
        ans = val * 100
        e2.insert(0, str(ans))
    except ValueError:
        e2.insert(0, "Error")

t1 = Label(text="Enter length in Meters:", fg="black", height=2, width=20)
t1.pack()

e1 = Entry(fg="black", bg="white", width=20)
e1.pack()

b1 = Button(win, text="Convert to CM", command=f1)
b1.pack(pady=10)

t2 = Label(text="Answer (cm):", fg="black", height=2, width=15)
t2.pack()

e2 = Entry(fg="black", bg="white", width=20)
e2.pack()

win.mainloop()