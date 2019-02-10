# If you want to have a top menu and instructions:
from tkinter import Canvas, Tk, Frame, Button, N, W, E, S, messagebox
import helpers
import utilities
import time
import random

# 0. Initialize global variables and functions:
UP_KEY = 8320768
DOWN_KEY = 8255233
LEFT_KEY = 8124162
RIGHT_KEY = 8189699
MOUSE_CLICK = '<Button-1>'
RIGHT_CLICK = '<Button-2>'
KEY_PRESS = '<Key>'

def make_circle(event):
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        20, 
        color='hotpink'
    )

def show_help_message():
   messagebox.showinfo('Help Menu', 'To add a circle, click the canvas')

# 1. Initialize window:
gui = Tk()
gui.title('Tour of options...')
gui.configure(background='hotpink')

# 2. Configure layout:
mainframe = Frame(gui, bg='#EEEEEE', padx=5, pady=5)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
gui.rowconfigure(0, weight=1) # row 0 takes up 10% of screen
gui.rowconfigure(1, weight=9) # row 1 takes up 90% of screen

# 3. Initialize close button:
# read about buttons:
# https://www.tutorialspoint.com/python3/tk_button.htm
info_btn = Button(
    mainframe,
    padx=5, 
    pady=5,
    text='HELP',
    command=show_help_message
)
info_btn.grid(column=0, row=0, sticky=E)

# 4. initialize canvas:
canvas_width = gui.winfo_screenwidth()
canvas_height = gui.winfo_screenheight() - 100
canvas = Canvas(
    gui, 
    width=canvas_width,
    height=canvas_height,
    background='white')
canvas.grid(column=0, row=1, sticky=W)
canvas.bind(MOUSE_CLICK, make_circle)  # add event handler


########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()