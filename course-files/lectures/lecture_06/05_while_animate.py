from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Using a while loop, please complete the following:
#   1. Make the circle smoothly move across the screen
#   2. Make it move backwards
#   3. Make it move vertically
#   4. Make it move diagonally
#   5. If it gets to the end, of the screen, make it reverse directions
#   6. Make it oscillate back and forth


# make circle
circle_id = shapes.make_circle(canvas, (100, 100), 40, color='hotpink')

# move circle
shapes.move(canvas, circle_id, x=60, y=0)
gui.update()
time.sleep(1)

# move circle
shapes.move(canvas, circle_id, x=60, y=0)
gui.update()
time.sleep(1)

# move circle
shapes.move(canvas, circle_id, x=60, y=0)
gui.update()
time.sleep(1)

# move circle
shapes.move(canvas, circle_id, x=60, y=0)
gui.update()
time.sleep(1)







########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()