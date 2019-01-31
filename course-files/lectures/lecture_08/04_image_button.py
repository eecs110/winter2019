# https://pythonspot.com/tk-window-and-button/

from tkinter import Tk, PhotoImage, Button
import os
 
root = Tk()
root.minsize(300,300)
root.geometry("320x100")
 
def callback():
    print("click!")
 
 
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'images', 'plus.png')
photo = PhotoImage(file=file_path)
b = Button(root, image=photo, command=callback, height=235, width=235)
b.pack()
 
root.mainloop()