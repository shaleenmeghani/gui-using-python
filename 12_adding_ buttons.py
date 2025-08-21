from tkinter import Tk,Label,Button

window=Tk()

window.title("gui with a button")

window.geometry("300x400")

window.iconbitmap("tree.ico")

L1=Label(window,text="press the button below",font=("arial",25,"bold"),fg="black",bg="red")
L1.pack(pady=5)

def logic_function():
    global L2
    L2=Label(window,text="hello from my GUI!!")
    L2.pack(pady=5)

B1=Button(window,text="press",command=logic_function)
B1.pack(pady=5)

def delete_undo():
    L2.destroy()

def close():
    window.destroy()

B2=Button(window,text="delete/undo",command=delete_undo).pack(pady=5)

B3=Button(window,text="close GUI",command=close).pack(pady=5)

window.mainloop()
