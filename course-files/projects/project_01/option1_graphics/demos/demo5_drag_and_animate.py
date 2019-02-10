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
MOUSE_DRAG = '<B1-Motion>'
MOUSE_CLICK = '<Button-1>'
data = []

canvas.create_text(
    (window_width / 2, window_height / 2), 
    text='Click or drag to create circles', 
    font=("Purisa", 32)
)

def make_circle(event):
    tag = 'circle_' + str(len(data))
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        random.uniform(10, 50), 
        color=None,
        tag=tag
    )
    data.append({
        'tag': tag,
        'speed': random.uniform(1, 5)
    })
canvas.bind(MOUSE_DRAG, make_circle)
canvas.bind(MOUSE_CLICK, make_circle)

# animation loop should come after everything else 
# (because while loop never terminates, and therefore nothing
# below the while loop will ever run):
while True:
    # print(data)
    for item in data:
        tag = item['tag']
        speed = -1 * item['speed']
        if utilities.get_bottom(canvas, tag) < 0:
            reset_position = window_height + utilities.get_width(canvas, tag)
            utilities.update_position(canvas, tag=tag, y=reset_position)
        utilities.update_position(canvas, tag=tag, x=0, y=speed)
    gui.update()
    time.sleep(0.002)