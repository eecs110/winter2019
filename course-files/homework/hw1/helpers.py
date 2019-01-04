'''
Documentation: http://effbot.org/tkinterbook/canvas.htm
Color Picker: https://coolors.co/
'''

# --------------------------------------------------------
# To be completed for Part 1 of Homework
# --------------------------------------------------------
# Text: Modify for Part 1.2.1.
def make_label(canvas):
    canvas.create_text(
        (210, 210), 
        text="Hello world!", 
        font=("Purisa", 32),
        anchor='nw'  # align to "northwest" corner
    )

# Oval: Modify for Part 1.2.2.
def make_oval(canvas):
    canvas.create_oval(
        [
            (50, 150), 
            (150, 250)
        ], # top left x-y, bottom right x-y
        fill='#FF4136',
        width=5
    )

# Polygon: Modify for Part 1.2.3.
def make_polygon(canvas):
    canvas.create_polygon(
        [
            (370, 150), 
            (630, 150), 
            (500, 350)
        ],  # list of x-y pairs
        width=2,
        fill='#BCD39C',
        smooth=True)  #make smooth false for angular polygon





# ---------------------------------------------------------------------
# Other functions / code samples that may be useful to you in some form
# ---------------------------------------------------------------------

# Lines
def make_solid_line(canvas):
    canvas.create_line(
        [
            (10, 0), 
            (210, 100), 
            (420, 0), 
            (630, 100)
        ],  # list of x-y pairs
        width=3)

def make_dashed_line(canvas):
    canvas.create_line(
        [
            (10, 100), 
            (210, 0), 
            (420, 100), 
            (630, 10)
        ], 
        fill="#3D9970", 
        dash=(4, 4), 
        width=3)

# curved:
def make_curvy_line(canvas):
    canvas.create_line(
        [
            (0,   100), 
            (50,  150), 
            (100, 100), 
            (150, 150), 
            (200, 100), 
            (250, 150), 
            (300, 100), 
            (350, 150), 
            (400, 100)
        ], 
        splinesteps=20,
        width=3, 
        smooth=True)

# Rectangle
def make_rectangle(canvas):
    canvas.create_rectangle(
        [
            (500, 25), 
            (650, 75)
        ],
        fill="#3D9970")

# Arc
def make_arc(canvas):
    canvas.create_arc(
        [
            (250, 50), 
            (450, 350)
        ],
        width=5,
        style='arc',
        outline='#0074D9'
    )

def make_grid(c, w, h):
    interval = 100

    # Delete old grid if it exists:
    c.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        c.create_line(i, 0, i, h, tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        c.create_line(0, i, w, i, tag='grid_line')

    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            c.create_oval(
                x - offset, 
                y - offset, 
                x + offset,  
                y + offset, 
                fill='black'
            )
            c.create_text(
                x + offset, 
                y + offset, 
                text="({0}, {1})".format(x, y),
                anchor="nw", 
                font=("Purisa", 8)
            )

def run_test(canvas):
    from creature import make_creature
    make_creature(
        canvas, (92, 115), width=85, primary_color='#5e6976', secondary_color='#1b324d')
    make_creature(
        canvas, (487, 110), width=101, primary_color='#bfdc65', secondary_color='#abb880')
    make_creature(
        canvas, (454, 423), width=141, primary_color='#aebb83', secondary_color='#227876')
    make_creature(
        canvas, (333, 227), width=99, primary_color='#94ba77', secondary_color='#3f5364')
    make_creature(
        canvas, (117, 314), width=91, primary_color='#648d8e', secondary_color='#afc272')
    make_creature(
        canvas, (199, 469), width=122, primary_color='#3f5364', secondary_color='#bfdc65')