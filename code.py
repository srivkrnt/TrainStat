from Tkinter import *
from tkMessageBox import *
import service

window = Tk()
window.title("SPOT YOUR TRAIN")
window.geometry("600x340")
window.resizable(0,0)

bg_img = PhotoImage(file="bg.gif")
Label(window, image=bg_img).place(x=-1, y=0)
Label(window, text="Train Number : ", font="Helvetica 11 bold").place(x=100 , y=100)
train_no = Entry(window, font="Helvetica 11 bold")
train_no.place(x=250 , y=100)

Label(window, text="Destination : ", font="Helvetica 11 bold").place(x=100, y=150)
Destination = Entry(window, font="Helvetica 11 bold")
Destination.place(x=250 , y=150)

Label(window, text="Phone Number : ", font="Helvetica 11 bold").place(x=100 , y=200)
mobile_no = Entry(window, font = "Helvetica 11 bold")
mobile_no.place(x=250 , y=200)


def start():
	service.check_status(train_no.get(), Destination.get().upper(), mobile_no.get())
	

submit = Button(window, text="SUBMIT", font="Helvetica 11 bold", bg="white", fg="green", command = start)
submit.place(x=280 , y=260)


window.mainloop()
