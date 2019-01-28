from tkinter import messagebox, Canvas, Tk
import random
import helpers

gui = Tk()
gui.title('Starry Night')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='#000022')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# TODO: the code below (lines 28-50) is repetitive. Replace it with a loop to make
# 1,000 stars that fill the entire canvas. Hints:
#   a) use a loop
#   b) use the random module, and in particular the random.uniform function to
#      to give each star a random (x, y) position and a random width.
#   c) bonus: Draw a constellation (Orion's Belt, Big Dipper, etc.) 

helpers.make_star(canvas, (655, 226), 1.5)
helpers.make_star(canvas, (435, 658), 0.1)
helpers.make_star(canvas, (276, 591), 1.4)
helpers.make_star(canvas, (226, 758), 0.1)
helpers.make_star(canvas, (75, 190), 2.0)
helpers.make_star(canvas, (92, 595), 1.3)
helpers.make_star(canvas, (38, 421), 2.7)
helpers.make_star(canvas, (376, 504), 0.6)
helpers.make_star(canvas, (740, 163), 0.8)
helpers.make_star(canvas, (987, 93), 0.6)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()