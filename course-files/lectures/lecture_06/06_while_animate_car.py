from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Challenge:
# Do the same thing as in 05_while_animate, but with
# all 4 shapes: 
#   1. Make the car smoothly drive across the screen
#   2. Make it drive backwards (on your own)
#   3. Make it drive vertically (on your own)
#   4. Make it drive diagonally (on your own)
#   5. If it gets to the end, of the screen, 
#      make it reverse directions (on your own)
#   6. Make it accelerate (on your own)


#make car:
top_id = shapes.make_rectangle(canvas, (100, 20), 100, 40)
bottom_id = shapes.make_rectangle(canvas, (50, 50), 200, 45)
wheel1_id = shapes.make_circle(canvas, (100, 100), 20, color='black')
wheel2_id = shapes.make_circle(canvas, (200, 100), 20, color='black')


# move car:
shapes.move(canvas, wheel1_id, x=60, y=0)
shapes.move(canvas, wheel2_id, x=60, y=0)
shapes.move(canvas, bottom_id, x=60, y=0)
shapes.move(canvas, top_id, x=60, y=0)
gui.update()
time.sleep(1)

# move car again:
shapes.move(canvas, wheel1_id, x=60, y=0)
shapes.move(canvas, wheel2_id, x=60, y=0)
shapes.move(canvas, bottom_id, x=60, y=0)
shapes.move(canvas, top_id, x=60, y=0)
gui.update()







########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()