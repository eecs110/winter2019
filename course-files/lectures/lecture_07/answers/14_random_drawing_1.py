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

# ## Challenge 1, Option 1 (of many):
# for i in range(50, 350, 50):
#     make_circle(canvas, (100, i), 25)

# # ## Challenge 1, Option 2 (of many):
# for i in range(0, 6):
#     make_circle(canvas, (100, 50 + i*50), 25)


## Challenge 2:
for j in range(1, 10):
    for i in range(0, 6):
        make_circle(canvas, (50*j, 50 + i*50), 25)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()