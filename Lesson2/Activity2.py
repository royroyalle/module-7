from tkinter import *
wind = Tk()
wind.geometry("250x300")
wind.title("Number Panel")

nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*' ]]
for i in range(4):
    wind.columnconfigure(i, weight= 1, minsize= 75)
    wind.rowconfigure(i, weight= 1, minsize= 50)
    for j in range(0, 3):
        frame = Frame(master= wind, relief="sunken", borderwidth= 1)
        frame.grid(row = i, column= j)
        label = Label(master=frame, text= nums[i][j], bg= "#76C1E7")
        label.pack(padx = 3, pady = 3)

wind.mainloop()