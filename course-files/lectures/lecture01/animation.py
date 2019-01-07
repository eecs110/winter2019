#!/usr/bin/python
from tkinter import *
import time
gui = Tk()
gui.geometry('800x600')
canvas = Canvas(gui, width=800, height=600)
canvas.pack()


ball1 = canvas.create_oval(50, 50, 100, 100, fill='pink')  # x1, y1, x2, y2
ball2 = canvas.create_oval(200, 50, 250, 100, fill='red')
ball3 = canvas.create_oval(0, 250, 50, 300, fill='teal')



# Animation loop
while True:
    canvas.move(ball1, 5, 5)   # adds 5 pixels to x-direction, 5 pixels to y-direction
    canvas.move(ball2, 0, 2)   # adds 2 pixels to y-direction
    canvas.move(ball3, 5, 0)   # adds 5 pixels to x-direction
    gui.update()
    time.sleep(0.015)

gui.title('Animated circles')
gui.mainloop()
