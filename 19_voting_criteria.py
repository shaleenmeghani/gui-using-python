from tkinter import Tk,Label,Entry,Button

w=Tk()
w.title("elidgibility to vote or not")
w.state("zoomed")

def check_logic():
    Age=E1.get()
    Id=E2.get()
    if int(Age)>=18 and Id=="yes":
        L3=Label(w,text="yes you can vote")
        L3.grid(row=3,column=0,columnspan=2)
    else:
        L3=Label(w,text="no you can't vote")
        L3.grid(row=3,column=0,columnspan=2)
    B.configure(state="disabled")

L1=Label(w,text="Enter your age")
E1=Entry()
L2=Label(w,text="Do you have an ID(yes/no)")
E2=Entry()
B=Button(w,text="check",command=check_logic)

L1.grid(row=0,column=0)
E1.grid(row=0,column=1)
L2.grid(row=1,column=0)
E2.grid(row=1,column=1)
B.grid(row=2,column=0,columnspan=2)

w.mainloop()



