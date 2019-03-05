from tkinter import Canvas, Tk

gui = Tk()
canvas = Canvas(gui, width=200, height=200, background='white')
canvas.pack()

canvas.create_rectangle(50, 25, 150, 75, fill="blue")

canvas.mainloop()