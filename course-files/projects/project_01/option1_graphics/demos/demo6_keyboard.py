'''
This demo shows you how you can create a new image by clicking the screen.
'''
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
UP_KEY = 8320768
DOWN_KEY = 8255233
LEFT_KEY = 8124162
RIGHT_KEY = 8189699
MOUSE_CLICK = '<Button-1>'
KEY_PRESS = '<Key>'
canvas.create_text(
    (window_width / 2, window_height / 2), 
    text='Click anywhere add a circle. Press arrow keys to move circle', 
    font=("Purisa", 32)
)

def make_circle(event):
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        20, 
        color='hotpink',
        tag='circle'
    )
    canvas.focus_set()

def move_circle(event):
    # print(event)
    distance = 10
    if event.keycode == UP_KEY:
        utilities.update_position(canvas, tag='circle', x=0, y=-distance)
    elif event.keycode == DOWN_KEY:
        utilities.update_position(canvas, tag='circle', x=0, y=distance)
    elif event.keycode == LEFT_KEY:
        utilities.update_position(canvas, tag='circle', x=-distance, y=0)
    elif event.keycode == RIGHT_KEY:
        utilities.update_position(canvas, tag='circle', x=distance, y=0)
    else:
        print(event.keycode)

canvas.bind(MOUSE_CLICK, make_circle) 
canvas.bind(KEY_PRESS, move_circle)


########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()