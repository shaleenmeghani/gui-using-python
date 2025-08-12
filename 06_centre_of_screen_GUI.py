from tkinter import Tk

window=Tk()

window.title("Centre of screen GUI")

gui_width=int(input("enter width for GUI:"))
gui_height=int(input("enter height for GUI"))

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

L=(screen_width-gui_width)//2
T=(screen_height-gui_height)//2

window.geometry(f'{gui_width}x{gui_height}+{L}+{T}')

window.mainloop()
