from tkinter import Tk,Label,Entry,Button

w=Tk()

w.title("C to F")
w.state("zoomed")

L=Label(w,text="Celsius to Fahrenheit..")
L.grid(row=0,column=0)
E=Entry()
E.grid(row=0,column=1)

def conversion():
    global L1
    c=E.get()
    f=(float(c)*9/5)+32
    L1=Label(w,text=f"{c}={f}")
    L1.grid(row=2,column=0,columnspan=2)
    B.configure(state="disabled")
    E.configure(state="disabled")
    B1.configure(state="normal")

def clear():
    E.delete(0, 'end')
    L1.grid_forget()
    B.configure(state="normal")
    E.configure(state="normal")

def close():
    w.destroy()

B=Button(w,text="convert",command=conversion)
B.grid(row=1,column=0)

B1=Button(w,text="clear",command=clear)
B1.grid(row=1,column=1)

B2=Button(w,text="close",command=close)
B2.grid(row=1,column=2)

w.mainloop()




