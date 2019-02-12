import os
import sys
dir_path = os.path.dirname(sys.argv[0])
file_and_path = os.path.join(dir_path, 'samples/moby_dick.txt')
f = open(file_and_path, 'r')
counter = 0
for line in f:
    words = line.split(' ')
    print(words)
    counter += len(words)

print('there are ', counter, 'words in the file.')