from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
win = Tk()
win.geometry("1000x1000")
win.title("Denomination Calculator")
win.configure(bg= "Light Blue")

upload = Image.open("bg.jpg")
upload.resize((500, 500))
image = ImageTk.PhotoImage(upload)

label = Label(win,  image= image, bg= "light blue")
label.place(x= 100, y= 20)
label1 = Label(win, text= "Welcome to Denomination Calculator", bg= "light blue")
label1.place(relx = 0.5, y= 340, anchor= CENTER)
def msg():
    Msgbox= messagebox.showinfo("Alert", "Do you want to calculate the denomination count")
    if Msgbox == "ok":
        topwin()

button1 = Button(win, text= "Lets get started", command= msg, bg= "brown", fg= "white")
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg= "light grey")
    top.geometry("600x350+50+50")
    label= Label(top, text= "Enter Total Amount", bg= "light grey")
    entry = Entry(top)
    lbl =   Label(top, text= "Number of notes in each denomination", bg= "light grey")
    l1 = Label(top, text= "2000", bg= "light grey")
    l2 = Label(top, text= "500", bg= "light grey")
    l3 = Label(top, text= "100", bg= "light grey")

    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)

    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount //100
            amount %- 100
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e1.insert(END, str(note2000))
            e2.insert(END, str(note500))
            e3.insert(END, note100)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    btn = Button(top, text= "Calculate",command= calculator, bg= "brown", fg= "white")
    label.place(x=230, y=50)
    entry.place(x= 200, y= 80)
    btn.place(x= 240, y=120)
    l1.place(x= 180, y= 200)
    l2.place(x= 180, y= 230)
    l3.place(x= 180, y = 260)
    e1.place(x= 270, y= 200)
    e2.place(x= 270, y= 230)
    e3.place(x= 270, y = 260)

    top.mainloop()           



win.mainloop()
