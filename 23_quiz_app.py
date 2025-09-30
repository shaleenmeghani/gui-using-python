from tkinter import Tk,Label,Button,Radiobutton,IntVar

w=Tk()
w.title("Quiz")
w.state("zoomed")

ans1=IntVar()
ans2=IntVar()
ans3=IntVar()
ans4=IntVar()
ans5=IntVar()

L1=Label(w,text="Question 1: Which Year is this ?")
R1=Radiobutton(w,text="2025",variable=ans1,value=1)
R2=Radiobutton(w,text="2024",variable=ans1,value=2)
R3=Radiobutton(w,text="2023",variable=ans1,value=3)
R4=Radiobutton(w,text="2022",variable=ans1,value=4)
L1.grid(row=0,column=0)
R1.grid(row=1,column=0)
R2.grid(row=2,column=0)
R3.grid(row=3,column=0)
R4.grid(row=4,column=0)

L2=Label(w,text="Question 2: Which Month is this ?")
R10=Radiobutton(w,text="Jan",variable=ans2,value=1)
R20=Radiobutton(w,text="Feb",variable=ans2,value=2)
R30=Radiobutton(w,text="July",variable=ans2,value=3)
R40=Radiobutton(w,text="October",variable=ans2,value=4)
L2.grid(row=6,column=0)
R10.grid(row=7,column=0)
R20.grid(row=8,column=0)
R30.grid(row=9,column=0)
R40.grid(row=10,column=0)

L3=Label(w,text="Question 3: Which date is closest ?")
R100=Radiobutton(w,text="22 Jan 2007",variable=ans3,value=1)
R200=Radiobutton(w,text="27 Jan 2011",variable=ans3,value=2)
R300=Radiobutton(w,text="23 Sept 2024",variable=ans3,value=3)
R400=Radiobutton(w,text="31 Dec 2024",variable=ans3,value=4)
L3.grid(row=12,column=0)
R100.grid(row=13,column=0)
R200.grid(row=14,column=0)
R300.grid(row=15,column=0)
R400.grid(row=16,column=0)

L4=Label(w,text="Question 4: Full form of EDITH ?")
R1000=Radiobutton(w,text="Even Dead I am The Hero",variable=ans4,value=1)
R2000=Radiobutton(w,text="Even Dead I The Hero",variable=ans4,value=2)
R3000=Radiobutton(w,text="I dont know",variable=ans4,value=3)
L4.grid(row=17,column=0)
R1000.grid(row=18,column=0)
R2000.grid(row=19,column=0)
R3000.grid(row=20,column=0)

L5=Label(w,text="Question is this the end?")
R10000=Radiobutton(w,text="Yes",variable=ans5,value=1)
R20000=Radiobutton(w,text="Maybe",variable=ans5,value=2)
R30000=Radiobutton(w,text="Never",variable=ans5,value=3)
L5.grid(row=22,column=0)
R10000.grid(row=23,column=0)
R20000.grid(row=24,column=0)
R30000.grid(row=25,column=0)

def check():
    sum=0
    choice1=ans1.get()
    choice2=ans2.get()
    choice3=ans3.get()
    choice4=ans4.get()
    choice5=ans5.get()

    global L6
    if choice1==1:
        sum+=1
    else:
        pass

    if choice2==4:
        sum+=1
    else:
        pass
    
    if choice3==4:
        sum+=1
    else:
        pass

    if choice4==1:
        sum+=1
    else:
        pass

    if choice5==2:
        sum+=1
    else:
        pass
    
    L6=Label(w,text=f"Your Score: {sum} Marks")
    L6.grid(row=29,column=0)
    B1.configure(state="disabled")
    B2.configure(state="normal")

def retest():
    ans1.set(0)
    ans2.set(0)
    ans3.set(0)
    ans4.set(0)
    ans5.set(0)
    L6.grid_forget()
    B1.configure(state="normal")
    B2.configure(state="disabled")

B1=Button(w,text="check score",command=check)
B1.grid(row=27,column=0,padx=5)
B2=Button(w,text="retest",command=retest,state="disabled")
B2.grid(row=27,column=1,padx=5)

w.mainloop()