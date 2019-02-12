import os
import sys
dir_path = os.path.dirname(sys.argv[0])
file_and_path = os.path.join(dir_path, 'samples/my_file.txt')
f = open(file_and_path, 'w')
f.write('hello world!')
f.close()