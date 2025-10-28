from tkinter import Tk,Label,Button,messagebox
from tkinter.ttk import Combobox

w=Tk()
w.title("movie ticket app")
w.geometry("300x300")

T=Label(w,text="Movie Tickets",font=("cambria",25,"bold"))
T.grid(row=0,column=0,pady=10,columnspan=2)

L1=Label(w,text="Day:",font=("cambria",12))
L1.grid(row=1,column=0,padx=10,sticky="w")
days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
DC=Combobox(w,value=days,font=("cambria",12))
DC.grid(row=1,column=1,padx=10,sticky="w")

L2=Label(w,text="Row:",font=("cambria",12))
L2.grid(row=2,column=0,padx=10,sticky="w")
row=["Top 5","Bottom 5","Mid"]
RC=Combobox(w,value=row)
RC.grid(row=2,column=1,padx=10)

def book_logic():
    cost=0
    day=str(DC.get())
    row=str(RC.get())
    if day=="monday" or day=="tuesday":
        cost+=100
    elif day=="wednesday" or day=="thursday":
        cost+=150
    elif day=="friday":
        cost+=175
    else:
        cost+=200
    
    if row=="Top 5":
        cost+=100
    elif row=="Bottom 5":
        cost+=0
    else:
        cost+=50

    messagebox.showinfo(title="Tickets Booked!!",message=f"total cost = {cost}")

B=Button(w,text="BOOK",command=book_logic)
B.grid(row=3,column=0,columnspan=2)

w.mainloop()