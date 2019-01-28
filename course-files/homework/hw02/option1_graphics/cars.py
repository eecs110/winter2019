from tkinter import Canvas, Tk
import time
import helpers

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# draw car (and give it a unique tag)
helpers.make_car(canvas, top_left=(0, 50), tag='car1')


# move car 50 pixels to the right:
time.sleep(1)
helpers.update_position(canvas, 'car1', x=50, y=0)
gui.update()

# move car 50 pixels to the right (exact same code):
time.sleep(1)
helpers.update_position(canvas, 'car1', x=50, y=0)
gui.update()

# move car 50 pixels to the right (exact same code):
time.sleep(1)
helpers.update_position(canvas, 'car1', x=50, y=0)
gui.update()










########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()