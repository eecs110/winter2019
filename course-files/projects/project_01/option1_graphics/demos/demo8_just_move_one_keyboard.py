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
# DOUBLE_CLICK = '<Double-Button-1>'  # couldn't get it to work
RIGHT_CLICK = '<Button-2>'
KEY_PRESS = '<Key>'
canvas.create_text(
    (window_width / 2, window_height / 2), 
    text='Click anywhere add a circle. Press arrow keys to move circle', 
    font=("Purisa", 32)
)

# need a global variable to store which item should be clicked:


active_tag = None
def select_circle(event):
    global active_tag
    canvas.focus_set()
    try:
        shape_ids = canvas.find_overlapping(
            event.x - 1, 
            event.y - 1, 
            event.x + 1, 
            event.y + 1)
        shape_id = shape_ids[-1] # get the top shape
        current_tag = canvas.gettags(shape_id)
        active_tag = current_tag[0]
        
        # just for debugging purposes:
        canvas.itemconfig(shape_id, fill='yellow')
    except:
        print('error: none found')


counter = 1
def make_circle(event):
    global counter
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        20, 
        color='hotpink',
        tag='circle_' + str(counter)
    )
    counter += 1
    canvas.focus_set()

def move_circle(event):
    distance = 10
    if event.keycode == UP_KEY:
        utilities.update_position(canvas, tag=active_tag, x=0, y=-distance)
    elif event.keycode == DOWN_KEY:
        utilities.update_position(canvas, tag=active_tag, x=0, y=distance)
    elif event.keycode == LEFT_KEY:
        utilities.update_position(canvas, tag=active_tag, x=-distance, y=0)
    elif event.keycode == RIGHT_KEY:
        utilities.update_position(canvas, tag=active_tag, x=distance, y=0)
    else:
        print(event.keycode)

canvas.bind(MOUSE_CLICK, make_circle) 
canvas.bind(KEY_PRESS, move_circle)
canvas.bind(RIGHT_CLICK, select_circle)


########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()