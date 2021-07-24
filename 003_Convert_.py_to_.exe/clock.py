'''
Python Program to Create Digital Clock
Author: Dr.Milan Parmar
'''

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

root.title("Digital clock")

def clock():
    tick = strftime("%H:%M:%S %p")

    label.config(text =tick)

    label.after(1000, clock)

label = Label(root, font = ("segoe", 60), foreground = "yellow", background = "black")

label.pack(anchor= "center")

clock()
mainloop()