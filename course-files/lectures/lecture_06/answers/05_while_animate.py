from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# make circle
circle_id = shapes.make_circle(canvas, (100, 100), 40, color='hotpink')

# move circle 30
shapes.move(canvas, circle_id, x=60, y=0)
gui.update()
time.sleep(1)

# move 30
shapes.move(canvas, circle_id, x=60, y=0)
gui.update()
time.sleep(1)

# move 30
shapes.move(canvas, circle_id, x=60, y=0)
gui.update()
time.sleep(1)

# move 30
shapes.move(canvas, circle_id, x=60, y=0)
gui.update()
time.sleep(1)







########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()