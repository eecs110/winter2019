from tkinter import Button, Checkbutton, Frame, Tk, N, W, E, S
from threading import Thread, Condition, Event
import psonic
import helpers
import thread_manager
import riffs

data = {
    'riff_1': {
        'length': 2,
        'riff': riffs.symbol_riff,
        'name': 'Cymbals'
    },
    'riff_1': {
        'length': 8,
        'riff': helpers.play_riff_2,
        'name': 'Twinkle Sound'
    },
}

condition = Condition()
threads = {
   'controller': thread_manager.start_looping_thread(riffs.controller_riff, condition, is_controller=True)
}

def toggle_riff_1():
    if threads.get('riff_1'):
        threads['riff_1'].set()
        del threads['riff_1']
    else:
        threads['riff_1'] = thread_manager.start_looping_thread(riffs.symbol_riff, condition)

def toggle_riff_2():
    if threads.get('riff_2'):
        threads['riff_2'].set()
        del threads['riff_2']
    else:
        threads['riff_2'] = thread_manager.start_looping_thread(helpers.play_riff_2, condition)


def toggle_riff_3():
    if threads.get('riff_3'):
        threads['riff_3'].set()
        del threads['riff_3']
    else:
        threads['riff_3'] = thread_manager.start_looping_thread(helpers.play_riff_3, condition)


def kill_threads():
    global threads
    for key in threads:
        threads[key].set()
    print('Killed all threads')

def make_interface():
    gui = Tk()
    gui.title("Song Player")
    mainframe = Frame(gui)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)
    gui.columnconfigure(0, weight=1)
    gui.rowconfigure(0, weight=1, pad=10)
    Checkbutton(
        mainframe, text="Play Cymbals", command=toggle_riff_1, padx=5, pady=5
    ).grid(column=0, row=0, sticky=W)
    Checkbutton(
        mainframe, text="Play Twinkle Sound", command=toggle_riff_2, padx=5, pady=5
    ).grid(column=0, row=1, sticky=W)
    Checkbutton(
        mainframe, text="Play 4 Beats", command=toggle_riff_3, padx=5, pady=5
    ).grid(column=0, row=2, sticky=W)
    Button(
        mainframe, text="kill threads", command=kill_threads, padx=5, pady=5
    ).grid(column=0, row=32, sticky=W)
    gui.mainloop()

make_interface()