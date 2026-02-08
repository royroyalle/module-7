from tkinter import *
wind = Tk()
wind.geometry("500x500")
wind.title("Pack, place and grid")

frame = Frame(master=wind, bg= "red", height= 100, width= 100)
frame.pack(pady= 0, side= RIGHT)

button = Button(master= wind, text= "Click this",bg="yellow", borderwidth= 10, relief="sunken")
button.pack(pady= 20)

button = Button(master= wind, text= "Click this",bg="yellow", borderwidth= 10, relief="sunken")
button.pack(pady= 20)

button = Button(master= wind, text= "Click this",bg="yellow", borderwidth= 10, relief="raised")
button.pack(pady= 20)

button = Button(master= wind, text= "Click this",bg="yellow", borderwidth= 10, relief="groove")
button.pack(pady= 20)

button = Button(master= wind, text= "Click this",bg="yellow", borderwidth= 10, relief="ridge")
button.pack(pady= 20)







wind.mainloop()