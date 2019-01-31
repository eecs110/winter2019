from tkinter import Canvas, Tk
import random
import shapes

gui = Tk()
gui.title('Circle')
# initialize canvas:
canvas = Canvas(gui, width=500, height=500, background='#FFFFFF')
canvas.pack()


########################## YOUR CODE BELOW THIS LINE ##############################

shapes.make_circle(canvas, (250, 250), 25, color=None, outline='black', stroke_width=2)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()