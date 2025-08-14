from tkinter import Tk,Label

window=Tk()

window.geometry("300x400")
window.iconbitmap("icon.ico")
window.title("text formating")
window.configure(bg="black")

L=Label(window,text="No Formating").pack()
L2=Label(window,text="yellow text",fg="yellow").pack()
L3=Label(window,text="white background",bg="white").pack()
L4=Label(window,text="green text with grey background",fg="green",bg="grey").pack()
L5=Label(window,text="new font",font=("Cambria",30)).pack()
L6=Label(window,text="omg effect!!",relief="sunken").pack()
L7=Label(window,text="disabled text",state="disabled").pack()

window.mainloop()