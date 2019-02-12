import os
import sys
dir_path = os.path.dirname(sys.argv[0])
file_and_path = os.path.join(dir_path, 'samples/my_file.txt')
f = open(file_and_path, 'a')
colors = ['red', 'pink', 'purple', 'orange', 'teal', 'blue']
for color in colors:
    f.write(color)
    f.write('\n')

f.close()