from tkinter import Tk,Label,Entry,Button
w=Tk()
w.title("simple interest calculator")
w.state("zoomed")

L1=Label(w,text="Enter Principle Amount",font=("cambria 20 bold"))
L1.grid(row=0,column=0)

E1=Entry(w,font=("cambria 20"))
E1.grid(row=0,column=1)

L2=Label(w,text="Enter Rate",font=("cambria 20 bold"))
L2.grid(row=1,column=0)

E2=Entry(w,font=("cambria 20"))
E2.grid(row=1,column=1)

L3=Label(w,text="Enter Time",font=("cambria 20 bold"))
L3.grid(row=2,column=0)

E3=Entry(w,font=("cambria 20"))
E3.grid(row=2,column=1)

def calculation():
    global L4
    B1.configure(state="disabled")
    B2.configure(state="normal")
    p=E1.get()
    r=E2.get()
    t=E3.get()
    si=(float(p)*float(r)*float(t))/100
    L4=Label(w,text=f"SI = {si}")
    L4.grid(row=4,column=0,columnspan=2)
    
def clear():
    E1.delete(0, "end")
    E2.delete(0, "end")
    E3.delete(0, "end")
    L4.grid_forget()
    B1.configure(state="normal")

def closewin():
    w.destroy()

B1=Button(w,text="calculate",command=calculation)
B1.grid(row=3,column=0)

B2=Button(w,text="clear",command=clear)
B2.grid(row=3,column=1)

B3=Button(w,text="close window",command=closewin)
B3.grid(row=3,column=2)

w.mainloop()
