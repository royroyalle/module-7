from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("500x500")
win.title("About Events ")
def handleEvent(event):
    print(event.char)

win.bind("<Key>", handleEvent)
button = Button(win, text= "submit")
button.pack()


win.bind("<Button-1>", lambda event:print(f"Left Click pressed", {event}))
win.bind("<Button-2>", lambda event:print(f"Mid Click pressed", {event}))
win.bind("<Button-3>", lambda event:print(f"Right Click pressed", {event}))
def f2 (event):
    messagebox.showwarning("Error Detected", "We Found A Virus In This File", )
def f1 (event):
    print("whatever I want to do")
button.bind("<Button-1>", f2)
win.mainloop()


