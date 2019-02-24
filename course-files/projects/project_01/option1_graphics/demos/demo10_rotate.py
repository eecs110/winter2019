import tkinter
import utilities
import time

gui = tkinter.Tk()
gui.title('Tour of options...')
w = h = 300

canvas = tkinter.Canvas(gui, width=w, height=h, background='white')
canvas.pack()

# my make creature function
def make_creature(canvas, center, size=100, tag='creature', fill='hotpink'):
    left_eye_pos = (center[0] - size / 4, center[1] - size / 5)
    right_eye_pos = (center[0] + size / 4, center[1] - size / 5)
    eye_width = eye_height = size / 10
    utilities.make_poly_circle(canvas, center, size, color=fill, tag=tag)
    utilities.make_poly_oval(canvas, left_eye_pos, eye_width, eye_height, color='black', tag=tag)
    utilities.make_poly_oval(canvas, right_eye_pos, eye_width, eye_height, color='black', tag=tag)
    utilities.make_line(canvas, [
        (center[0] - size / 2, center[1] + size / 3), 
        (center[0], center[1] + size / 1.2), 
        (center[0] + size / 2, center[1] + size / 3)
    ], curvy=True, tag=tag)

make_creature(canvas, (150, 150), tag='c1')

while True:
    gui.update()
    time.sleep(0.02)
    utilities.rotate(canvas, 'c1', degrees=1, origin=(150, 150))
    gui.update()
gui.mainloop()