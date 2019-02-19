# How many representatives does each state have in the House?
import sys
import os
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'legislators-current.csv')
# End VS Code Hack:

f = open(file_path, 'r', encoding='utf8', errors='ignore')

reps_by_state_by_party = {}
for line in f.readlines():
    cells = line.split(',')
    gender = cells[7]
    house_or_senate = cells[8]
    state = cells[9]
    party = cells[12]
    # print(gender, house_or_senate, state, party)
    if house_or_senate == 'rep':
        if reps_by_state_by_party.get(state) is None:
            reps_by_state_by_party[state] = {}
        if reps_by_state_by_party[state].get(party) is None:
            reps_by_state_by_party[state][party] = 0
        reps_by_state_by_party[state][party] += 1
        

#sorted_keys = sorted(reps_by_state_by_party, key=reps_by_state_by_party.get, reverse=True)
for key in reps_by_state_by_party:
    print(key + ':')
    d_or_r = reps_by_state_by_party[key]
    for k in d_or_r:
        print(k + ':', d_or_r[k])