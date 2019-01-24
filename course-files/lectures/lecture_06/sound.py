from psonic import *
from threading import Thread, Condition, Event

def loop_foo():
  play (E4, release = 0.5)
  sleep (0.5)


def loop_bar():
  sample (DRUM_SNARE_SOFT)
  sleep (1)


def live_loop_1(condition,stop_event):
    while not stop_event.is_set():
        with condition:
            condition.notifyAll() #Message to threads
        loop_foo()

def live_loop_2(condition,stop_event):
    while not stop_event.is_set():
        with condition:
            condition.wait() #Wait for message
        loop_bar()



condition = Condition()
stop_event = Event()
live_thread_1 = Thread(name='producer', target=live_loop_1, args=(condition,stop_event))
live_thread_2 = Thread(name='consumer1', target=live_loop_2, args=(condition,stop_event))


live_thread_1.start()
live_thread_2.start()

counter = 0
while True:
    input("Press Enter to continue...")
    if counter % 2 == 0:
        stop_event.set()
    else:
        stop_event = Event()
        Thread(name='producer', target=live_loop_1, args=(condition,stop_event)).start()
        Thread(name='consumer1', target=live_loop_2, args=(condition,stop_event)).start()
    counter += 1