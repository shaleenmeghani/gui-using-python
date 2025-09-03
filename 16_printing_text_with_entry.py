from tkinter import Tk,Entry,Label,Button

w=Tk()

w.title("GUI with input buttons and output")
w.state("zoomed")

L=Label(w,text="enter your name:")
L.pack()
E=Entry()
E.pack()

def name_output():
    name=E.get()
    L1=Label(w,text=f"good morning, {name}")
    L1.pack()

B=Button(w,text="print",command=name_output).pack()

w.mainloop()
