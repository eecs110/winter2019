# refactor this code so that it uses a function
def print_colors(c1, c2, c3, times):
    for i in range(times):
        print(c1)
    for i in range(times):
        print(c2)
    for i in range(times):
        print(c3)

print_colors('red', 'yellow', 'green', 2)
print_colors('blue', 'orange', 'pink', 3)
print_colors('gray', 'black', 'white', 1)
print_colors('maroon', 'purple', 'teal', 4)