from tkinter import Tk,Label,Button
w=Tk()
w.title("columnspan")
w.geometry("700x700")
w.iconbitmap("tree.ico")

L1=Label(text="column 1",font=("calibri 15 bold")).grid(row=0,column=0)
L2=Label(text="column 2",font=("calibri 15 bold")).grid(row=0,column=1)
L3=Label(text="column 3",font=("calibri 15 bold")).grid(row=0,column=2)
B=Button(text="click!!").grid(row=1,column=0,columnspan=3)

w.mainloop()
