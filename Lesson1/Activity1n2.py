from tkinter import *
wind = Tk()
wind.geometry("600x400")
wind.title("First Tkinter App")
label = Label(wind,text="Hello!, Get inf credits by telling your password")
label.pack()
def bt():
    content = entry.get()
    label.config(text= f"You have been scammed by telling us your password which is- {content}")
entry = Entry(wind)
entry.pack()
button = Button(wind, text= "Click this to get inf credits", command=bt)
button.pack()
text = Text(wind)
text.pack()

wind.mainloop()