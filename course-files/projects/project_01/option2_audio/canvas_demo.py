from tkinter import Canvas, Tk
import time

gui = Tk()
gui.title('My Mixer')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=500, height=500, background='#999999')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
speed = 1
def callback(event):
    print(event.char, 'pressed')
    print(event)
canvas.focus_set()
canvas.bind("<1>", lambda event: canvas.focus_set())
canvas.bind("<Key>", callback)
########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()