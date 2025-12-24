import time
from tkinter import *
def clock():
        obj=time.localtime()
        display_time=time.strftime("%H:%M:%S %p",obj)
        label_time.config(text=display_time)
        main.after(1000,clock)
main=Tk()
main.title("Digital Clock")
label_time=Label(main,font=("Consolas",60),bg="black",fg="cyan")
label_time.pack()
clock()
main.mainloop()