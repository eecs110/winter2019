# http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm 
from tkinter import Canvas, Tk
import helpers
import utilities
import time
import random

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_CLICK = '<Button-1>'
RIGHT_CLICK = '<Button-2>'
canvas.create_text(
    (window_width / 2, window_height / 2), 
    text='Click to create circle. Right-click to remove circle', 
    font=("Purisa", 32)
)
def make_circle(event):
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        20, 
        color='hotpink'
    )

def remove_circle(event):
    # http://effbot.org/tkinterbook/canvas.htm#reference
    shape_ids = canvas.find_overlapping(
        event.x - 1, 
        event.y - 1, 
        event.x + 1, 
        event.y + 1)
    for id in shape_ids:
        canvas.delete(id)

canvas.bind(MOUSE_CLICK, make_circle)
canvas.bind(RIGHT_CLICK, remove_circle)

########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()