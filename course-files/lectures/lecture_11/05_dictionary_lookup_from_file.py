import json
import sys
import os

# read lookup table from a file:
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'state_capitals.json')
f = open(file_path, 'r')
capital_lookup = json.loads(f.read())


def get_state_capital(lookup, state):
    return lookup[state]


# use lookup table to answer some questions:
print('The capital of Florida is:', get_state_capital(capital_lookup, 'Florida'))
print('The capital of Illinois is:', get_state_capital(capital_lookup, 'Illinois'))
print('The capital of California is:', get_state_capital(capital_lookup, 'California'))
print('The capital of Massachusetts is:', get_state_capital(capital_lookup, 'Massachusetts'))