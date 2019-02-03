def print_message(key):
    if key == 0:
        print(key, ':', 'zero')
    elif key == 1:
        print(key, ':', 'one')
    elif key < 10:
        print(key, ':', 'less than 10')
    elif key == 10.0:
        print(key, ':', 'equal to 10.0')
    elif key > 10:
        print(key, ':', 'more than 10')
    else:
        print(key, ':', 'IDK')

print_message(5)
print_message(10.0)
print_message(11)
print_message(True)
print_message(False)
print_message(0.0)