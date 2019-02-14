# How many representatives does each state have in the House?
import sys
import os
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'legislators-current.csv')
# End VS Code Hack:

f = open(file_path, 'r', encoding='utf8', errors='ignore')
for line in f.readlines():
    cells = line.split(',')
    print(cells)