from tkinter import*

root2 = Tk()

root2.geometry("200x120")
root2.title("Menu")



def enter1():
	root2.destroy()
	import management


def enter2():
	root2.destroy()
	import PriceFile


labels = Label(root2, text="Bill")
labels.grid(row=1, sticky=E)

press_btn = Button(root2, text="Press Here", command= enter1)
press_btn.grid(row=1, column=1)

label21 = Label(root2, text="Change Price")
label21.grid(row=2,sticky=E)

press1_btn = Button(root2, text="Press Here", command= enter2)
press1_btn.grid(row=2, column=1)

root2.mainloop()
