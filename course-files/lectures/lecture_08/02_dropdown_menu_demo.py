# http://effbot.org/tkinterbook/optionmenu.htm
from tkinter import ttk, Tk, N, W, E, S, StringVar
import psonic

root = Tk()
root.title("Song Player")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# function that gets called when dropdown selection changes:
def switch_synth(selected_text):
    print(selected_text)
    # set synth according to request:
    if selected_text == available_synths[0]:
        psonic.use_synth(psonic.PIANO)
    elif selected_text == available_synths[1]:
        psonic.use_synth(psonic.PROPHET)
    elif  selected_text == available_synths[2]:
        psonic.use_synth(psonic.SAW)
    
    psonic.play(55)

available_synths = [
    'Piano',
    'Prophet',
    'Saw'
]
# required to do in documentation:
# not necessarily clear why this is a requirement, but the designers
# of this library require that we do this so the options menu works:
my_synth = StringVar(mainframe)

# frame, variable, default value, menu options, function to execute:
menu = ttk.OptionMenu(mainframe, my_synth, available_synths[0], *available_synths, command=switch_synth)
menu.grid(column=1, row=1, sticky=W)

root.mainloop()