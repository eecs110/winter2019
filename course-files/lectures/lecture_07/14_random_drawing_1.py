from tkinter import Canvas, Tk
import random

gui = Tk()
gui.title('Circle')
# initialize canvas:
canvas = Canvas(gui, width=500, height=500, background='#000022')
canvas.pack()

def make_circle(canvas, center, radius, color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )
########################## YOUR CODE BELOW THIS LINE ##############################

# Challenge: How could I rewrite the following code using a for loop and a range function?
# Challenge 2: How do I make rows of circles?
# On your own: Try to make the drawings in the slides

make_circle(canvas, (100, 50), 25)
make_circle(canvas, (100, 100), 25)
make_circle(canvas, (100, 150), 25)
make_circle(canvas, (100, 200), 25)
make_circle(canvas, (100, 250), 25)
make_circle(canvas, (100, 300), 25)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()