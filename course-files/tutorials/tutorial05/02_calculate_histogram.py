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
for line in f.readlines():
    print(line)