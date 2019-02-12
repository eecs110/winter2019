import os
import sys
dir_path = os.path.dirname(sys.argv[0])
file_and_path = os.path.join(dir_path, 'samples/moby_dick.txt')
f = open(file_and_path, 'r')
line_num = 1
for line in f:
    words = line.split(' ')
    for word in words:
        if word.upper() == 'MOBY':
            print(line_num, word)
            continue
    line_num += 1

