from tkinter import Canvas, Tk
import random
import shapes

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500, background='#FFFFFF')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################


for i in range(10):
    shapes.make_circle(canvas, (250, 25 + i*25), 25 + i*25, color=None, outline='black', stroke_width=1)



########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()