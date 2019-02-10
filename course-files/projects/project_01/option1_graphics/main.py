from tkinter import Canvas, Tk
import helpers
import utilities
import time

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# sample code to make a creature:
helpers.make_creature(canvas, (100, 100))
helpers.make_landscape_object(canvas, (0, window_height))

########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()