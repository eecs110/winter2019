# http://effbot.org/tkinterbook/button.htm
from tkinter import ttk, Tk, N, W, E, S, StringVar
import psonic


    
root = Tk()
root.title("Song Player")
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

psonic.use_synth(psonic.PIANO)
def play_c():
    psonic.play(48)

def play_d():
    psonic.play(50)

def play_e():
    psonic.play(52)

def play_f():
    psonic.play(53)

ttk.Button(mainframe, text="C", command=play_c).grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="D", command=play_d).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text="E", command=play_e).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="F", command=play_f).grid(column=4, row=1, sticky=W)


root.mainloop()