from tkinter import Button, Frame, Tk, N, W, E, S
from threading import Thread, Condition, Event
import psonic
import helpers

tick = psonic.Message()

state = {
    'riff_1': False,
    'riff_2': False,
    'riff_3': False,
    'speed': 2
}
loops = []

@psonic.in_thread
def main_loop():
    while True:
        tick.cue()
        helpers.play_base_beat(state['speed'])

@psonic.in_thread
def riff_1_loop():
    while True:
        tick.sync()
        if state['riff_1']:
            helpers.play_riff_1(state['speed'])

@psonic.in_thread
def riff_2_loop():
    while True:
        tick.sync()
        if state['riff_2']:
            helpers.play_riff_2(state['speed'])

@psonic.in_thread
def riff_3_loop():
    while True:
        tick.sync()
        if state['riff_3']:
            helpers.play_riff_3(state['speed'])

def start_music_loop(state):
    loops.append(riff_1_loop())
    loops.append(riff_2_loop())
    loops.append(riff_3_loop())
    main_loop()
    print(loops)

def toggle_riff_1():
    state['riff_1'] = not state['riff_1']

def toggle_riff_2():
    state['riff_2'] = not state['riff_2']

def toggle_riff_3():
    state['riff_3'] = not state['riff_3']

def kill_threads():
    pass

def make_interface():
    gui = Tk()
    gui.title("Song Player")
    mainframe = Frame(gui)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)
    gui.columnconfigure(0, weight=1)
    gui.rowconfigure(0, weight=1, pad=10)
    Button(
        mainframe, text="play riff 1", command=toggle_riff_1, padx=5, pady=5
    ).grid(column=0, row=0, sticky=W)
    Button(
        mainframe, text="play riff 2", command=toggle_riff_2, padx=5, pady=5
    ).grid(column=0, row=1, sticky=W)
    Button(
        mainframe, text="play riff 3", command=toggle_riff_3, padx=5, pady=5
    ).grid(column=0, row=2, sticky=W)
    Button(
        mainframe, text="kill threads", command=kill_threads, padx=5, pady=5
    ).grid(column=0, row=32, sticky=W)
    gui.mainloop()

start_music_loop(state)
make_interface()