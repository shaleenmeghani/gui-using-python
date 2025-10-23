from tkinter import Tk,Label,Entry,Button,messagebox

w=Tk()

w.title("divider app")
w.geometry("400x400")
w.configure(bg="brown")

T=Label(w,text="Divider",font=("cambria",45,"bold"),bg="brown",fg="white")
T.grid(row=0,column=0,sticky="nsew")

L=Label(w,text="enter value for denominator:",bg="brown",fg="white",font=("cambria",20))
L.grid(row=1,column=0,pady=3)
E=Entry()
E.grid(row=2,column=0,padx=100)

L2=Label(w,text="enter value for numerator:",bg="brown",fg="white",font=("cambria",20))
L2.grid(row=3,column=0,pady=3)
E2=Entry()
E2.grid(row=4,column=0,padx=100)

def calculate():
    d=int(E.get())
    n=int(E2.get())
    if n==0:
        messagebox.showerror(title="Oh No!!",message="numerator can never be zero!")
    elif d==0:
        messagebox.showinfo(title="Soooo!",message="anything divided by zero is zero!")
    elif n==0 and d==0:
        messagebox.showerror(title="Oh No!!",message="numerator can never be zero but you even entered denominator as 0 to :)!!")
    else:
        ans=d/n
        messagebox.showinfo(title="Soooo!",message=f"ans = {ans}")

B=Button(w,text="divide",bg="grey",command=calculate)
B.grid(row=5,column=0,pady=7)

w.mainloop()