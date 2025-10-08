from tkinter import Tk,Frame,Label

w=Tk()

w.title("GUI with Frames")
w.geometry("500x200")

F1=Frame(w,width=250,height=200,bg="red")
F2=Frame(w,width=250,height=200,bg="black")
F1.grid_propagate(False)
F2.grid_propagate(False)
F1.grid(row=0,column=0)
F2.grid(row=0,column=1)

L1=Label(F1,text="Red",bg="red",fg="black",font=("italic 50 bold"))
L2=Label(F2,text="Black",bg="black",fg="white",font=("italic 50 bold"))
L1.grid(row=0,column=0,sticky="nsew")
L2.grid(row=0,column=0,sticky="nsew")

w.mainloop()