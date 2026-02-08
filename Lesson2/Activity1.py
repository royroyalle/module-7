from tkinter import *

window = Tk()
window.title('Login App')
window.geometry('400x400')

main_container = Frame(master=window, height=200, width=360, bg="#d0efff")

tag_name = Label(main_container, text="Full Name", bg="#3895D3", fg='white', width=12)
tag_email = Label(main_container, text="Email Id", bg="#3895D3", fg='white', width=12)
tag_pass = Label(main_container, text="Enter Password", bg="#3895D3", fg='white', width=12)

input_user = Entry(main_container)
input_mail = Entry(main_container)
input_secret = Entry(main_container, show="*")

def handle_submit():
    username = input_user.get()
    header = "Hey " + username
    body = "\nCongratulations for your new account!"
    output_area.insert(END, header)
    output_area.insert(END, body)

output_area = Text(bg="#BEBEBE", fg="black")

submit_cmd = Button(text="Create Account", command=handle_submit, bg="red")

main_container.place(x=20, y=0)
tag_name.place(x=20, y=20)
input_user.place(x=150, y=20)
tag_email.place(x=20, y=80)
input_mail.place(x=150, y=80)
tag_pass.place(x=20, y=140)
input_secret.place(x=150, y=140)
submit_cmd.place(x=130, y=210)
output_area.place(y=250)

window.mainloop()