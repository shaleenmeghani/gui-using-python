from tkinter import Tk,Label,Button,Checkbutton,IntVar

w=Tk()
w.title("checkbox prediction")
w.geometry("400x400")

india=IntVar()
australia=IntVar()
newzealand=IntVar()
southafrica=IntVar()

L1=Label(w,text="Predict World Cup Finalists:")
C1=Checkbutton(w,text="India",bg="blue",fg="orange",variable=india,onvalue=1,offvalue=0)
C2=Checkbutton(w,text="Australia",bg="yellow",fg="green",variable=australia,onvalue=1,offvalue=0)
C3=Checkbutton(w,text="NewZealand",bg="black",fg="blue",variable=newzealand,onvalue=1,offvalue=0)
C4=Checkbutton(w,text="South Africa",bg="yellow",fg="green",variable=southafrica,onvalue=1,offvalue=0)
L1.grid(row=0,column=0)
C1.grid(row=1,column=0)
C2.grid(row=2,column=0)
C3.grid(row=3,column=0)
C4.grid(row=4,column=0)

def close():
    w.destroy()

def check():
    global L2
    if india.get()==1 and australia.get()==0 and newzealand.get()==0 and southafrica.get()==1:
        L2=Label(w,text="you guessed it right!!")
        B1.configure(state="disabled")
        B2.configure(state="disabled")
        B3=Button(w,text="close",command=close)
        B3.grid(row=5,column=2)
    else:
        L2=Label(w,text="you guessed it wrong!!,try again..")
        B1.configure(state="disabled")
        B2.configure(state="normal")
    L2.grid(row=8,column=0)

def retry():
    india.set(0)
    australia.set(0)
    newzealand.set(0)
    southafrica.set(0)
    L2.grid_forget()
    B1.configure(state="normal")
    B2.configure(state="disabled")

B1=Button(w,text="check",command=check)
B2=Button(w,text="retry",command=retry,state="disabled")
B1.grid(row=5,column=0)
B2.grid(row=5,column=1)

w.mainloop()