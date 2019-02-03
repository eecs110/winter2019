from tkinter import Canvas, Tk
import random
import shapes
import math

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500, background='#FFFFFF')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

center_x = 250
center_y = 250
distance_from_center = 60
radius_of_individual_circle = 20 
num_circles = 20
for i in range(num_circles):
    # calculate new position of x and y
    radians = 360 / num_circles * i * (math.pi / 180)
    dy = distance_from_center * math.sin(radians)
    dx = distance_from_center * math.cos(radians)
    x = center_x + dx
    y = center_y - dy
    shapes.make_circle(canvas, (x, y), radius_of_individual_circle, color=None, outline='black', stroke_width=1)


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()