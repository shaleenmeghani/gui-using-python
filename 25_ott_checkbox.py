from tkinter import Tk,Label,Button,Checkbutton,IntVar

w=Tk()

w.title("OTT Price Calculator")
w.geometry("600x600")

n=IntVar()
a=IntVar()
y=IntVar()
j=IntVar()

L1=Label(w,text="Choose your subscribed OTT's:")
C1=Checkbutton(w,text="Netflix",variable=n,onvalue=1,offvalue=0)
C2=Checkbutton(w,text="Amazon Prime",variable=a,onvalue=1,offvalue=0)
C3=Checkbutton(w,text="Youtube Premium",variable=y,onvalue=1,offvalue=0)
C4=Checkbutton(w,text="Jio Hotstar",variable=j,onvalue=1,offvalue=0)

def calculation():
    cost=0
    if n.get()==1:
        cost+=1000
    if a.get()==1:
        cost+=800
    if y.get()==1:
        cost+=200
    if j.get()==1:
        cost+=100
    global L2
    L2=Label(w,text=f"total cost of your subscribed ott channels = Rs{cost}")
    L2.grid(row=6,column=0)
    B.configure(state="disabled")

B=Button(w,text="calculate cost",command=calculation)

L1.grid(row=0,column=0)
C1.grid(row=1,column=0)
C2.grid(row=2,column=0)
C3.grid(row=3,column=0)
C4.grid(row=4,column=0)
B.grid(row=5,column=0)

w.mainloop()