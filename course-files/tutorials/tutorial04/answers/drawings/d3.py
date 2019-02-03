from tkinter import Canvas, Tk
import random
import shapes

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500, background='#FFFFFF')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

for i in range(20):
    x = 250
    y = 250 + i * 5
    r = 2 + i * 2
    shapes.make_circle(canvas, (x, y), r, color=None, outline='black', stroke_width=1)

for i in range(20):
    x = 250
    y = 250 - i * 5
    r = 2 + i * 2
    shapes.make_circle(canvas, (x, y), r, color=None, outline='black', stroke_width=1)

for i in range(20):
    x = 250 + i * 5
    y = 250
    r = 2 + i * 2
    shapes.make_circle(canvas, (x, y), r, color=None, outline='black', stroke_width=1)

for i in range(20):
    x = 250 - i * 5
    y = 250
    r = 2 + i * 2
    shapes.make_circle(canvas, (x, y), r, color=None, outline='black', stroke_width=1)

########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()