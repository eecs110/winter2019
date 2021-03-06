# How many representatives does each state have in the House?
import sys
import os
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'legislators-current.csv')
# End VS Code Hack:

f = open(file_path, 'r', encoding='utf8', errors='ignore')

reps_by_state = {}
for line in f.readlines():
    cells = line.split(',')
    house_or_senate = cells[8]
    state = cells[9]
    if house_or_senate == 'rep':
        if reps_by_state.get(state) is None:
            reps_by_state[state] = 0
        reps_by_state[state] += 1

sorted_keys = sorted(reps_by_state, key=reps_by_state.get, reverse=True)
for key in sorted_keys:
    print(key + ':', reps_by_state[key])