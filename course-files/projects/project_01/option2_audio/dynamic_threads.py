import psonic
from threading import Thread, Condition, Event
import helpers
import random

live_threads = {}

def controller_riff():
    psonic.sample(psonic.DRUM_SNARE_SOFT)
    psonic.sleep(0.5)

def snare_riff():
    psonic.sample(psonic.DRUM_SNARE_SOFT)
    psonic.sleep(1)

def symbol_riff():
    psonic.sample(psonic.DRUM_CYMBAL_OPEN)
    psonic.sleep(1)

def start_thread(sample, condition, is_controller=False):
    stop_event = Event()
    Thread(
        target=start_loop, args=(condition, stop_event, sample, is_controller)
    ).start()
    return stop_event

def start_loop(condition, stop_event, sample, is_controller=False):
    while not stop_event.is_set():
        with condition:
            if is_controller:
                condition.notifyAll() # notify
            else:
                condition.wait() # wait for message
        sample()

condition = Condition()
live_threads['controller'] = start_thread(controller_riff, condition, is_controller=True)

counter = 0
while True:
    input("Press Enter to continue...")
    if counter % 3 == 0:
        print('turning thread off...')
        if live_threads.get('loop_bar'):
           live_threads['loop_bar'].set()
    elif counter % 3 == 1:
        print('turning thread on...')
        loops = [snare_riff, symbol_riff, helpers.play_riff_2]
        riff = loops[random.randint(0, len(loops) - 1)]
        live_threads['loop_bar'] = start_thread(riff, condition)
    counter += 1