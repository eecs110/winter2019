from tkinter import Canvas, Tk
from helpers import *  # means that you are importing all of the functions
                       # in the helpers.py file

# initialize window
gui = Tk()
gui.title('Creature')
screen_width = 700
screen_height = 350
c = Canvas(
    gui, width=screen_width, height=screen_height, background='white')
c.pack()
########################## YOUR CODE BELOW THIS LINE ############################## 





# --------------------------------------------------------
# To be completed for Part 1 of Homework
# --------------------------------------------------------
make_label(c)               # Modify for Part 1.2.1.
make_oval(c)                # Modify for Part 1.2.2.
make_polygon(c)             # Modify for Part 1.2.3.

# ---------------------------------------------------------------------
# Other functions / code samples that may be useful to you in some form
# ---------------------------------------------------------------------
make_rectangle(c)
make_arc(c)
make_curvy_line(c)
make_dashed_line(c)
make_solid_line(c)

# for convenience:
make_grid(c, screen_width, screen_height)





########################## YOUR CODE ABOVE THIS LINE ############################## 
c.mainloop()
