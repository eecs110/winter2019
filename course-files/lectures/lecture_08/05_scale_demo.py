# http://effbot.org/tkinterbook/scale.htm
from tkinter import Tk, Scale

root = Tk()

def print_selection(speed):
    print(speed)

w = Scale(root, from_=0, to=5, resolution=0.5, command=print_selection)
w.pack()

root.mainloop()