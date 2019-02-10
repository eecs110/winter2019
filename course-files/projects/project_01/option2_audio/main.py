from threading import Thread, Condition, Event
import helpers

def main_loop(condition):
    while True:
        with condition:
            condition.notifyAll() #Message to threads
        helpers.play_base_beat(speed)

def riff_1_loop(condition):
    while True:
        with condition:
            condition.wait() #Wait for message
        if riff_1_on:
            helpers.play_riff_1(speed)

def riff_2_loop(condition):
    while True:
        with condition:
            condition.wait() #Wait for message
        if riff_2_on:
            helpers.play_riff_2(speed)

def riff_3_loop(condition):
    while True:
        with condition:
            condition.wait() #Wait for message
        if riff_3_on:
            helpers.play_riff_3(speed)

def show_menu():
    print('*' * 80)
    print('Select option from the menu')
    print('1 - toggle riff 1 (', 'on' if riff_1_on else 'off', ')')
    print('2 - toggle riff 2 (', 'on' if riff_2_on else 'off', ')')
    print('3 - toggle riff 3 (', 'on' if riff_3_on else 'off', ')')
    print('4 - slow down')
    print('5 - speed up')
    print('q - quit')
    print('*' * 80)



def start_music_loop():
    condition = Condition()
    Thread(name='riff1', target=riff_1_loop, args=(condition,)).start()
    Thread(name='riff2', target=riff_2_loop, args=(condition,)).start()
    Thread(name='riff3', target=riff_3_loop, args=(condition,)).start()
    Thread(name='producer', target=main_loop, args=(condition,)).start()


####################
# GLOBAL VARIABLES #
####################
speed = 2
riff_1_on = True
riff_2_on = True
riff_3_on = True
command = ''
start_music_loop()
while command.upper() != 'Q':
    show_menu()
    command = input("What would you like to do? ")
    if command == '1':
        if riff_1_on:
            riff_1_on = False
        else:
            riff_1_on = True
    elif command == '2':
        if riff_2_on:
            riff_2_on = False
        else:
            riff_2_on = True
    elif command == '3':
        if riff_3_on:
            riff_3_on = False
        else:
            riff_3_on = True
    elif command == '4':
        speed *= 1.1
    elif command == '5':
        riff_1_on = True
        speed /= 1.1
    elif command.upper() == 'Q':
        print('Stop!')
        break