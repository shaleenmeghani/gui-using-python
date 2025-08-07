from tkinter import Tk

window=Tk()

name=input("enter title for GUI:")
window.title(name)

width=int(input("enter width:"))
height=int(input("enter height:"))
top=int(input("enter top value:"))
left=int(input("enter left value:"))

window.geometry(f"{width}x{height}+{top}+{left}")

window.mainloop()