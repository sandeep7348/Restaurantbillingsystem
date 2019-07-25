from tkinter import *
import tkinter.messagebox

root1 = Tk()
root1.geometry("420x220")
root1.title("Login Page")

name = StringVar()
password = StringVar()


def enterthedetailss():
    if name.get() == "Sandeep" and password.get() == "1234":
        root1.destroy()
        import changeprice
    else:
        tkinter.messagebox.showinfo('Error', 'Authentication Failed')
        name.set("")
        password.set("")


def destroy():
    root1.destroy()
def timer():
    root1.destroy()
    import Timetill



label = Label(root1, font=('Helvetica', 50) ,text="Login", fg="steel blue", bd=10, anchor='w')
label.grid(row=0)

label1 = Label(root1,font=('Helvetica',16), text="Username")
label2 = Label(root1, font=('Helvetica',16), text="Password")

entry1 = Entry(root1, textvariable=name)
entry2 = Entry(root1, textvariable=password)

label1.grid(row=1, sticky=NW)
label2.grid(row=2, sticky=NW)
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)

enter_btn = Button(root1, text="Enter", command=enterthedetailss)
enter_btn.grid(row=3, column=1)

exit_btn = Button(root1, padx=2, text="Exit", command=destroy)
exit_btn.grid(row=3, column=2)
timer_btn=Button(root1,text="Timer",command=timer)
timer_btn.grid(row=3,column=3)
root1.mainloop()
