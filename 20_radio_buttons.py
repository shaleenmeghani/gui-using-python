from tkinter import Tk,Label,Radiobutton,Button,IntVar

w=Tk()
w.title("RadioButtons")
w.state("zooomed")

vegetable=IntVar()
cyn=IntVar()
oyn=IntVar()

L1=Label(w,text="choose vegetable")
R1=Radiobutton(w,text="Tomato",variable=vegetable,value=1)
R2=Radiobutton(w,text="Capsicum",variable=vegetable,value=2)
R3=Radiobutton(w,text="Onion",variable=vegetable,value=3)
R4=Radiobutton(w,text="Corn",variable=vegetable,value=4)
L1.grid(row=0,column=0)
R1.grid(row=1,column=0)
R2.grid(row=2,column=0)
R3.grid(row=3,column=0)
R4.grid(row=4,column=0)

L2=Label(w,text="do you want chilliflakes?")
R10=Radiobutton(w,text="yes",variable=cyn,value=1)
R20=Radiobutton(w,text="no",variable=cyn,value=2)
L2.grid(row=6,column=0)
R10.grid(row=7,column=0)
R20.grid(row=8,column=0)

L3=Label(w,text="do you want oregano?")
R100=Radiobutton(w,text="yes",variable=oyn,value=1)
R200=Radiobutton(w,text="no",variable=oyn,value=2)
L3.grid(row=10,column=0)
R100.grid(row=11,column=0)
R200.grid(row=12,column=0)

def new():
    vegetable.set(0)
    cyn.set(0)
    oyn.set(0)
    B1.configure(state="disabled")
    B2.configure(state="normal")


def order():
    B1.configure(state="normal")
    B2.configure(state="disabled")
    B3.configure(state="normal")

    v=vegetable.get()
    c=cyn.get()
    o=oyn.get()

    if v==1:
        vname="Tomato"
    elif v==2:
        vname="Capsicum"
    elif v==3:
        vname="Onion"
    else:
        vname="Corn"
    
    if c==1:
        cchoice="with chilliflakes"
    else:
        cchoice="without chilliflakes"
    
    if o==1:
        ochoice="with oregano"
    else:
        ochoice="without oregano"

    L4=Label(w,text=f"your order for {vname} pizza ,{cchoice},{ochoice} is placed..:)")
    L4.grid(row=17,column=0,columnspan=2)

def exitGUI():
    w.destroy()

B1=Button(w,text="New",command=new,state="disabled")
B1.grid(row=14,column=0)
B2=Button(w,text="Order",command=order)
B2.grid(row=14,column=1)
B3=Button(w,text="Exit",command=exitGUI)
B3.grid(row=15,column=2)

w.mainloop()



