from tkinter import Canvas, Tk, ttk, StringVar, N, S, E, W

    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
canvas = Canvas(mainframe, width=500, height=500, background='#999999')
canvas.grid(column=1, row=3, sticky=W, columnspan=3)

def callback(event):
    print(event.char, 'pressed')
    print(event)
canvas.focus_set()
canvas.bind("<1>", lambda event: canvas.focus_set())
canvas.bind("<Key>", callback)


ttk.Button(mainframe, text="Quit", command=root.destroy).grid(column=3, row=4, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()

root.mainloop()