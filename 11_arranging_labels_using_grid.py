from tkinter import Tk,Label

window=Tk()

window.geometry("500x500+100+100")

window.title("arranging labels with grid")

window.iconbitmap("tree.ico")

L1=Label(window,text="Label 1",font=("Arial",20),fg="red",bg="black")
L2=Label(window,text="Label 2",font=("Arial",10),fg="green",bg="red")
L3=Label(window,text="Label 3",font=("Arial",15),fg="blue",bg="grey")
L4=Label(window,text="Label 4",font=("Arial",7),fg="cyan",bg="grey")
L5=Label(window,text="Label 5",font=("Arial",11),fg="magenta",bg="red")
L6=Label(window,text="Label 6",font=("Arial",25),fg="yellow",bg="black")

L1.grid(row=0,column=0)
L2.grid(row=0,column=1)
L3.grid(row=0,column=2)
L4.grid(row=1,column=0)
L5.grid(row=1,column=1)
L6.grid(row=1,column=2)

window.mainloop()