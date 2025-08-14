from tkinter import Tk,Label

window=Tk()

window.geometry("300x400")
window.iconbitmap("icon.ico")
window.title("GUI with a title")

L=Label(window,text="my first label")#text is not a variable but a parameter
L.pack(pady=15)

L2=Label(window,text="will this text variable work??").pack() #better to write as line 12 as this will return None

window.mainloop()