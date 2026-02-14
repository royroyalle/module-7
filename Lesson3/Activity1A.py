from tkinter import *
win = Tk()
win.title("Event Handler")
win.geometry("100x100")

def handle_keypress(event):
    print(event.char)

win.bind("<Key>", handle_keypress)
def handle_click(event):
    print("/The button was clicked ")
button = Button(text= "Click Me!")
button.pack()
button.bind("<Button-1>", handle_click)
win.mainloop()