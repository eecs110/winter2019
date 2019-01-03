'''
Documentation: http://effbot.org/tkinterbook/canvas.htm
Color Picker: https://coolors.co/
'''
from tkinter import Canvas, Tk
# initialize window
gui = Tk()
gui.title('Creature')
winWidth = gui.winfo_screenwidth()
winHeight = gui.winfo_screenheight()
canvas = Canvas(gui, width=winWidth, height=winHeight, background='#DDDDDD')
canvas.pack()


########################################################
# YOUR CODE HERE:

#------#
# LINE #
#------#
canvas.create_line(10, 0, 210, 100, 420, 0, 630, 100, width=3)
canvas.create_line(10, 100, 210, 0, 420, 100, 630, 10, fill="#3D9970", dash=(4, 4), width=3)

# curved:
canvas.create_line(
    0,   100, 
    50,  150, 
    100, 100, 
    150, 150, 
    200, 100, 
    250, 150, 
    300, 100, 
    350, 150, 
    400, 100, 
    splinesteps=20,
    width=3, 
    smooth=True)

#-----------#
# RECTANGLE #
#-----------#
canvas.create_rectangle(500, 25, 650, 75, fill="#3D9970")

#------#
# OVAL #
#------#
canvas.create_oval(
    50,  # left
    150,  # top
    150,  # right
    250,  # bottom
    fill='#FF4136',
    width=5
)

#---------#
# Polygon #
#---------#
canvas.create_polygon(
    170, 300,   # alternates x1, y1, x2, y2, x3, y3, ...
    430, 300,   
    300, 500,
    width=2,
    fill='#001f3f',
    smooth=True)

canvas.create_polygon(
    370, 500,   # alternates x1, y1, x2, y2, x3, y3, ...
    630, 500,   
    500, 700,
    width=2,
    fill='#BCD39C',
    smooth=False)

#-----#
# ARC #
#-----#
canvas.create_arc(
    150,  # left
    150,  # top
    250,  # right
    250,  # bottom
    fill='#0074D9',
    width=2,
    style='pieslice'
)

canvas.create_arc(
    250,  # left
    50,  # top
    450,  # right
    350,  # bottom
    width=5,
    style='arc',
    outline='#0074D9'
)

#-------#
# IMAGE #
#-------#
# JPG (a little more complicated)
from PIL import Image, ImageTk
jpg_image = Image.open("picasso.jpg")               # open it
jpg_image.thumbnail((200, 200), Image.ANTIALIAS)    # scale it
tk_image = ImageTk.PhotoImage(jpg_image)            # convert it to correct format
canvas.create_image((800, 400), image=tk_image)     # draw it on the canvas


#------#
# TEXT #
#------#
canvas.create_text(300, 250, text="Hello world!", font=("Purisa", 22))



# END YOUR CODE
########################################################

# Do not accidentally delete:
canvas.mainloop()