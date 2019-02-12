import tkinter
import psonic
import riffs
import threader

####################
# Global Variables #
####################
# 1. controller controls the pace of the other loops and samples:
#    similar to a metronome.
controller = threader.SonicPiController(tempo=1, riff=riffs.controller_riff)

# 2. loops play continuously until they are stopped
loop_1 = threader.SonicPiLoop(controller, riffs.riff_8)
loop_2 = threader.SonicPiLoop(controller, riffs.riff_1)
loop_3 = threader.SonicPiLoop(controller, riffs.riff_3)
loop_4 = threader.SonicPiLoop(controller, riffs.riff_4)
loop_5 = threader.SonicPiLoop(controller, riffs.riff_8)

# 3. samples only play once
sample_1 = threader.SonicPiSample(controller, riffs.riff_5)
sample_2 = threader.SonicPiSample(controller, riffs.riff_6)
sample_3 = threader.SonicPiSample(controller, riffs.play_harley_sound)
sample_4 = threader.SonicPiSample(controller, riffs.riff_7)
sample_5 = threader.SonicPiSample(controller, riffs.riff_1)

# 4. other global variables
CLOSE_WINDOW = 'WM_DELETE_WINDOW'
gui = None
canvas = None


#############
# Functions #
############# 
def toggle_loop_1():
    if loop_1.is_running():
        loop_1.stop()
    else:
        loop_1.start()

def toggle_loop_2():
    if loop_2.is_running():
        loop_2.stop()
    else:
        loop_2.start()
   
def toggle_loop_3():
    # your job
    pass

def toggle_loop_4():
    # your job
    pass

def toggle_loop_5():
    # your job
    pass

def make_faster():
    # your job (extra credit: update the controller's tempo)
    pass

def make_slower():
    # your job (extra credit: update the controller's tempo)
    pass

def kill_threads_and_close():
    # when you close the window, this function gets
    # called to kill all of the threads:
    print('Killing all threads...')
    loop_1.stop()
    loop_2.stop()
    loop_3.stop()
    loop_4.stop()
    loop_5.stop()
    controller.stop()
    gui.destroy()


def make_interface():
    # set up window and layout:
    global gui
    global canvas
    gui = tkinter.Tk()
    gui.title('Audio Mixer')

    # --------------------
    # 1. set up gui layout
    # --------------------
    win_width = 750
    win_height = 450
    gui.geometry('{}x{}'.format(win_width, win_height))
    gui.grid_rowconfigure(0, weight=1)
    gui.grid_rowconfigure(1, weight=10)
    gui.grid_columnconfigure(0, weight=1)
    gui.grid_columnconfigure(1, weight=3)

    # ---------------------------------------------
    # 2. create all of the main frames / containers
    # ---------------------------------------------
    header_frame = tkinter.Frame(gui, bg='#EEE', pady=3)
    header_frame.grid(row=0, column=0, sticky="nsew", columnspan=2)

    left_frame = tkinter.Frame(gui, pady=3)
    left_frame.grid(row=1, column=0, sticky="nsew")

    center_frame = tkinter.Frame(gui, pady=3)
    center_frame.grid(row=1, column=1, sticky="nsew")
    center_frame.grid_rowconfigure(0, weight=9)
    center_frame.grid_rowconfigure(0, weight=1)
    center_frame.grid_columnconfigure(0, uniform='1')

    # -----------------------------
    # 3. Header Frame: Add Controls
    # -----------------------------
    header_frame.grid_columnconfigure(0, weight=1)
    title = tkinter.Label(header_frame, bg='#EEE', text='Audio Mixer')
    title.grid(row=0, sticky="EWNS")
    tkinter.Button(
        header_frame,
        text='+',
        command=make_faster,
        padx=5,
    ).grid(column=1, row=0, sticky="E")

    tkinter.Button(
        header_frame,
        text='-',
        command=make_slower,
        padx=5,
    ).grid(column=2, row=0, sticky="E")

    # ----------------------------
    # 4. Left Frame: Loop Controls
    # ----------------------------
    tkinter.Checkbutton(
        left_frame,
        text='Loop 1',
        command=toggle_loop_1,
        padx=5, 
        pady=5
    ).grid(column=0, row=0, sticky="NW")

    tkinter.Checkbutton(
        left_frame,
        text='Loop 2',
        command=toggle_loop_2,
        padx=5, 
        pady=5
    ).grid(column=0, row=1, sticky="NW")  # don't forget to increment the row number

    tkinter.Checkbutton(
        left_frame,
        text='Loop 3',
        command=toggle_loop_3,
        padx=5, 
        pady=5
    ).grid(column=0, row=2, sticky="NW")  # don't forget to increment the row number

    tkinter.Checkbutton(
        left_frame,
        text='Loop 4',
        command=toggle_loop_4,  # which function should fire
        padx=5, 
        pady=5
    ).grid(column=0, row=3, sticky="NW")

    tkinter.Checkbutton(
        left_frame,
        text='Loop 5',
        command=toggle_loop_5,  # which function should fire
        padx=5, 
        pady=5
    ).grid(column=0, row=4, sticky="NW")

    # --------------------------------
    # 5. Center Frame: Sample Controls
    # --------------------------------
    canvas = tkinter.Canvas(
        center_frame, background='#999999', width=650, bd=0
    )
    canvas.grid(row=0, column=0, sticky="NSEW", columnspan=5)
    tkinter.Button(
        center_frame,
        text='Sample 1',
        command=sample_1.start,  # which function should fire
        padx=5, 
        pady=5
    ).grid(column=0, row=1, sticky="EW", padx=4, pady=4)

    tkinter.Button(
        center_frame,
        text='Sample 2',
        command=sample_2.start,  # which function should fire
        padx=5, 
        pady=5
    ).grid(column=1, row=1, sticky="EW", padx=4, pady=4)

    tkinter.Button(
        center_frame,
        text='Sample 3',
        command=sample_3.start,  # which function should fire
        padx=5, 
        pady=5
    ).grid(column=2, row=1, sticky="EW", padx=4, pady=4)

    tkinter.Button(
        center_frame,
        text='Sample 4',
        command=sample_4.start,  # which function should fire
        padx=5, 
        pady=5
    ).grid(column=3, row=1, sticky="EW", padx=4, pady=4)

    tkinter.Button(
        center_frame,
        text='Sample 5',
        command=sample_5.start,  # which function should fire
        padx=5, 
        pady=5
    ).grid(column=4, row=1, sticky="EW", padx=4, pady=4)

    # -------------
    # Final touches
    # -------------
    gui.protocol(CLOSE_WINDOW, kill_threads_and_close)
    gui.mainloop()



###################
# Invoke Function #
###################
make_interface()