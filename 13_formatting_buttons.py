from tkinter import Tk,Button

window=Tk()

window.title("button formatting")
window.geometry("700x400")
window.iconbitmap("tree.ico")

B1=Button(window,text="default button").pack()
B2=Button(window,text="button with fg and bg",fg="grey",bg="red").pack()
B3=Button(window,text="button with text style",font="Arial 20 bold italic").pack()
B4=Button(window,text="button with active and default fg/bg",bg="blue",fg="white",activebackground="grey",activeforeground="red").pack()
B5=Button(window,text="button with border",bd=10).pack()
B6=Button(window,text="disabled!!",state="disabled").pack()

window.mainloop()