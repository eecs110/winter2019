import os
import sys
dir_path = os.path.dirname(sys.argv[0])
file_and_path = os.path.join(dir_path, 'samples/moby_dick.txt')
f = open(file_and_path, 'r', encoding='utf8')
for line in f:
    print(line)