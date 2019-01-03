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
gui = Tk()
gui.title('Creature')
winWidth = gui.winfo_screenwidth()
winHeight = gui.winfo_screenheight()
canvas = Canvas(gui, width=winWidth, height=winHeight, background='silver')
canvas.pack()
############################### YOUR CODE HERE ############################## 







####################### DO NOT WRITE BELOW THIS LINE ########################


# Do not accidentally delete:
canvas.mainloop()