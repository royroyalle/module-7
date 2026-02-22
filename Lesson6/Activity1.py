from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
win = Tk()
win.geometry("500x500")
win.title("RMS App")
upload = Image.open("bg.jpg")
upload = upload.resize((550, 550))
image = ImageTk.PhotoImage(upload)

label = Label(win,  image= image, bg= "light blue")
label.place(x= 0, y= 0)
label1 = Label(win, text= "Restaurant Order Management",font= 50, bg= "white")
label1.place(relx = 0.5, y= 50, anchor= CENTER)
def msg():
    Msgbox= messagebox.showinfo("Confirmation", "Proceed to Checkout?")
    if Msgbox == "ok":
        topwin()

button1 = Button(win, text= "Enter Checkout", command= msg, bg= "brown", fg= "white")
button1.place(relx=0.5, y=80, anchor= CENTER)

def topwin():
    top = Toplevel()
    top.title("RMS Checkout")
    top.configure(bg= "light grey")
    top.geometry("600x350+50+50")
    label= Label(top, text= "List of Items",font= 10, bg="light grey")
    def calc():
        try:
            a1 = int(e1.get())
            a2 = int(e2.get())
            a3 = int(e3.get())
            a4 = int(e4.get())
            a5 = int(e5.get())
            a6 = int(e6.get())
            cb = 200
            ff = 300
            sd = 30
            ck = 75
            cn = 40
            re = 90
            cb1 = a1*cb
            ff1 = a2*ff
            sd1 = a3*sd
            ck1 = a4*ck
            cn1 = a5*cn
            re1 = a6*re
            entry2 = (cb1+ff1+sd1+ck1+cn1+re1)
            entry.delete(0, END)
            entry.insert(END, str(entry2))
        except ValueError:
            messagebox.showerror("Error", "Please enter properly or we will make you clean the dishes")
    button2 =Button(top, text= "Checkout Amount To Pay",font= 10, bg= "light grey", command= calc)
    entry = Entry(top)
    l1 = Label(top, text= "Cheeseburger", bg= "light grey")
    l2 = Label(top, text= "French Fries", bg= "light grey")
    l3 = Label(top, text= "Salad", bg= "light grey")
    l4 = Label(top, text= "Coke", bg= "light grey")
    l5 = Label(top, text= "Cheese Nuggets", bg= "light grey")
    l6 = Label(top, text= "Rice", bg= "light grey")

    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)
    e4 = Entry(top)
    e5 = Entry(top)
    e6 = Entry(top)

    label.place(x=50, y=20)
    l1.place(x= 50, y= 100)
    l2.place(x= 50, y= 130)
    l3.place(x= 50, y = 160)
    l4.place(x=50, y=190)
    l5.place(x=50, y= 220)
    l6.place(x=50, y=250)
    e1.place(x=150, y=100)
    e2.place(x= 150, y= 130)
    e3.place(x= 150, y = 160)
    e4.place(x= 150,y= 190)
    e5.place(x= 150, y= 220)
    e6.place(x= 150, y= 250)
    button2.place(x=50, y=300)
    entry.place(x=250, y=300)
    top.mainloop()    
win.mainloop()