'''
This demo shows you how to put any image onto a canvas and resize it
using a function that I made called make_image.
'''
from tkinter import Canvas, Tk
import helpers
import utilities
import time

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# make a background feature from an image:
utilities.make_image(
    canvas, 'images/rock-bg.png', # path to image
    position=(-30, window_height + 10),
    anchor='sw',
    size=(500, 300)
)

# make a creature feature from a feature:
utilities.make_image(
    canvas, 'images/jelly.png', # path to image
    position=(window_width / 2 - 100, window_height / 2 - 200),
    anchor='nw',
    size=(200, 400)
)

########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()