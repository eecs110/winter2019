def print_menu(red, yellow, blue):
    print('-' * 30)
    print('The current color is', get_color(red, yellow, blue).upper())
    print('-' * 30)
    print('1 - Toggle Red', '(' + str(red) + ')')
    print('2 - Toggle Yellow', '(' + str(yellow) + ')')
    print('3 - Toggle Blue', '(' + str(blue) + ')')
    print('4 - Quit')
    print('-' * 30)
    print()

def get_color(red, yellow, blue):
    if red and yellow and blue: 
        return 'black'
    elif red and yellow:
        return 'orange'
    elif red and blue:
        return 'purple'
    elif yellow and blue:
        return 'green'
    elif red:
        return 'red'
    elif yellow:
        return 'yellow'
    elif blue:
        return 'blue'
    else:
        return 'white'



red_switch = False
yellow_switch = False
blue_switch = False

status = ''
while status.upper() != 'Q':
    print_menu(red_switch, yellow_switch, blue_switch)
    status = input('What would you like to do (1-4)? ')
    print('')
    if status == '1':
        red_switch = not red_switch
    elif status == '2':
        yellow_switch = not yellow_switch
    elif status == '3':
        blue_switch = not blue_switch
    elif status == '4':
        print('exiting loop...')
        break

    
