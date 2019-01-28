from threading import Thread, Condition, Event
import helpers

def start_music_loop():
    condition = Condition()
    Thread(name='riff1', target=riff_1_loop, args=(condition,)).start()
    Thread(name='riff2', target=riff_2_loop, args=(condition,)).start()
    Thread(name='riff3', target=riff_3_loop, args=(condition,)).start()
    Thread(name='producer', target=main_loop, args=(condition,)).start()


def main_loop(condition):
    while True:
        with condition:
            condition.notifyAll() #Message to threads
        helpers.play_base_beat(speed)


def riff_1_loop(condition):
    while True:
        with condition:
            condition.wait() #Wait for message
        helpers.play_riff_1(speed)


def riff_2_loop(condition):
    while True:
        with condition:
            condition.wait() #Wait for message
        helpers.play_riff_2(speed)


def riff_3_loop(condition):
    while True:
        with condition:
            condition.wait() #Wait for message
        helpers.play_riff_3(speed)


def show_menu():
    input('\nPress any key to continue...')
    header_length = 28
    print()
    print('*' * header_length)
    print('Select option from the menu')
    print('*' * header_length)
    print('1 - toggle riff 1 (' + ('on' if riff_1_on else 'off') + ')')
    print('2 - toggle riff 2 (' + ('on' if riff_2_on else 'off') + ')')
    print('3 - toggle riff 3 (' + ('on' if riff_3_on else 'off') + ')')
    print('4 - slow down')
    print('5 - speed up')
    print('q - quit')
    print('*' * header_length)
    print()


####################
# GLOBAL VARIABLES #
####################
speed = 2.0
riff_1_on = True
riff_2_on = True
riff_3_on = True
start_music_loop()


###################
# USER INPUT LOOP #
###################
command = ''
while command.upper() != 'Q':
    show_menu()
    command = input("What would you like to do? ")
    print('\nYou selected:')
    if command == '1':
        # replace print statement with code that toggles riff_1 on / off
        print('\n1 - toggle riff_1 on / off...')
    elif command == '2':
        # replace print statement with code that toggles riff_2 on / off
        print('\n2 - toggle riff_3 on / off...')
    elif command == '3':
        # replace print statement with code that toggles riff_3 on / off
        print('\n3 - toggle riff_3 on / off...')
    elif command == '4':
        # replace print statement with code that slows down the music
        print('\n4 - slow down the music...')
    elif command == '5':
        # replace print statement with code that speeds up the music
        print('\n5 - speed up the music...')
    elif command.upper() == 'Q':
        print('Stop!')
        break