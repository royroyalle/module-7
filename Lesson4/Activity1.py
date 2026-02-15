from tkinter import *
from tkinter import filedialog
win = Tk()
win.geometry("600x600")
win.title("Text Editor | Note Pad")

def save_file():
    file = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("text files, *txt"), ("All files", "*.*")])
    if file:
        data = textbox.get("1.0", END)
        with open(file, "a") as f:
            f.write(str(data))
        

def open_file():
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r") as f:
            content = f.read()
            textbox.insert("1.0", content)
            textbox.delete("1.0", END)


menuframe = Frame(win)
menuframe.pack(side= 'left')
sb = Button(win, text= "Save", width= 10,  command= save_file)
sb.pack()
se = Button(win, text= "Open", width= 10,  command= open_file)
se.pack()

textbox= Text(win)
textbox.pack(fill= "both", expand= True)



win.mainloop()