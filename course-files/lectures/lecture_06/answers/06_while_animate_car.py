from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################


top_id = shapes.make_rectangle(canvas, (100, 20), 100, 40)
bottom_id = shapes.make_rectangle(canvas, (50, 50), 200, 45)

wheel1_id = shapes.make_circle(canvas, (100, 100), 20, color='black')
wheel2_id = shapes.make_circle(canvas, (200, 100), 20, color='black')

while True:
    shapes.move(canvas, wheel1_id, x=3, y=0)
    shapes.move(canvas, wheel2_id, x=3, y=0)
    shapes.move(canvas, bottom_id, x=3, y=0)
    shapes.move(canvas, top_id, x=3, y=0)
    gui.update()
    time.sleep(.001)







########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()