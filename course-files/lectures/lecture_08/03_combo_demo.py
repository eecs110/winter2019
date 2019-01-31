# from tkinter import *
from tkinter import ttk, Tk, N, W, E, S, StringVar
import psonic
  
root = Tk()
root.title("Song Player")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

speed = 0.5

def switch_synth(selected_text):
    print(selected_text)
    if selected_text == available_synths[0]:
        psonic.use_synth(psonic.PIANO)
    elif selected_text == available_synths[1]:
        psonic.use_synth(psonic.PROPHET)
    elif  selected_text == available_synths[2]:
        psonic.use_synth(psonic.SAW)


def play_song_1():
    psonic.play(52)
    psonic.sleep(speed)
    psonic.play(54)
    psonic.sleep(speed)

def play_song_2():
    psonic.play(55)
    psonic.sleep(speed)
    psonic.play(57)
    psonic.sleep(speed)



available_synths = [
    'Piano',
    'Prophet',
    'Saw'
]
synth = StringVar(mainframe)
menu = ttk.OptionMenu(mainframe, synth, available_synths[0], *available_synths, command=switch_synth)
menu.grid(column=1, row=1, sticky=W)

ttk.Button(mainframe, text="play song 1", command=play_song_1).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="play song 2", command=play_song_2).grid(column=1, row=3, sticky=W)


root.mainloop()