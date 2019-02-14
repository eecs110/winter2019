import os
import sys
dir_path = os.path.dirname(sys.argv[0])
md_source = os.path.join(dir_path, 'samples/moby_dick.txt')
md_destination = os.path.join(dir_path, 'samples/moby_dick_line_numbers.txt')

source_file = open(md_source, 'r')
destination_file = open(md_destination, 'w', encoding='utf8')

linenum = 1
for line in source_file:
    destination_file.write(str(linenum) + '. ')
    destination_file.write(line)
    linenum += 1
source_file.close()
destination_file.close()