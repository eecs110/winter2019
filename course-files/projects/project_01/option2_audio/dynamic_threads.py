import psonic
from threading import Thread, Condition, Event
import helpers
import random
import riffs
import thread_manager

condition = Condition()
live_threads = {
    'controller': thread_manager.start_looping_thread(riffs.controller_riff, condition, is_controller=True)
}

counter = 0
while True:
    input("Press Enter to continue...")
    if counter % 3 == 0:
        print('turning thread off...')
        if live_threads.get('loop_bar'):
           live_threads['loop_bar'].set()
    elif counter % 3 == 1:
        print('turning thread on...')
        loops = [riffs.snare_riff, riffs.symbol_riff]
        riff = loops[random.randint(0, len(loops) - 1)]
        live_threads['loop_bar'] = thread_manager.start_looping_thread(riff, condition)
    else:
        print('sample!')
        thread_manager.start_sample_thread(riffs.sample_riff)
    counter += 1