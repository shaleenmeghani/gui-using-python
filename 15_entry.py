from tkinter import Tk,Entry

w=Tk()
w.title("taking input from user")
w.state("zoomed")

E=Entry()
E.pack()

E1=Entry(width=10)
E1.pack()

E2=Entry(font=("cambria 25 bold"))
E2.pack()

w.mainloop()

