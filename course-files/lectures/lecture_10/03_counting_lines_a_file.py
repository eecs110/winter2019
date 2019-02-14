import os
import sys
dir_path = os.path.dirname(sys.argv[0])
file_and_path = os.path.join(dir_path, 'samples/moby_dick.txt')
f = open(file_and_path, 'r', encoding='utf8')
counter = 0
for line in f:
    counter += 1

print('there are ', counter, 'lines in the file.')