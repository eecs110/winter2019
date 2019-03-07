# write a program that reads the contents of the Food_Establishment_Violations
# for the City of Evanston and counts the number of violations that have occurred
# in each category. The, print out the category, and the number of violations

# VS Code Hack:
import sys
import os
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'Food_Establishment_Violations.csv')
# End VS Code Hack:

f = open(file_path, 'r', encoding='utf8', errors='ignore')
tally = {}
for line in f.readlines():
    # use the split function to split each row by the cell (each cell is separated by a ," delimiter)
    cells = line.split(',"')
    if len(cells) > 1:
        # get the second cell:
        violation = cells[1]

        # split the second cell by the colon to get the violation category
        code = violation.split(':')[0]

        # add that key to the dictionary if it doesn't exist:
        if not tally.get(code):
            tally[code] = 0
        
        # increment by 1
        tally[code] += 1

# output all of the results at the end:
for key in tally.keys():
    print(key, tally[key], sep=':')