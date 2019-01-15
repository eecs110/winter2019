'''
Documentation: http://effbot.org/tkinterbook/canvas.htm
Color Picker: https://coolors.co/
Some inspiration:
   * https://www.youtube.com/watch?v=yh_A09CrT68
   * https://www.shutterstock.com/image-vector/cute-animals-cartoon-illustrator-flat-design-247667131
   * https://www.pinterest.com/pin/118782508901992203/
   * https://goo.gl/hKewyL 
'''
from tkinter import Canvas, Tk
from helpers import make_grid       # import the make_grid function (for debugging)
from creature import make_creature  # import your make_creature function 


gui = Tk()
gui.title('Your Creature')

# code to detect the screen's width and height:
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

# initialize the canvas
canvas = Canvas(gui, width=screen_width, height=screen_width, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# In this section, add code to call your make_creature function
# Use different arguments for color, position, and size

make_creature(canvas)
make_grid(canvas, screen_width, screen_height)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()
