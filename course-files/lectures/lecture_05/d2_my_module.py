'''
Things to notice:
    1. These are all function defintions, but there are no function calls.
       In other words, none of these functions will run unless they are
       invoked.
    2. Modules can import other modules. Note that this module is making use
       of the os module
'''

import os


def get_hypotenuse(side1, side2):
    return (side1 ** 2 + side2 ** 2) ** 0.5

def get_area(side1, side2):
    area = (side1 * side2) / 2
    return area

def get_perimeter(side1, side2):
    perimeter = 2 * side1 + 2 * side2
    return perimeter

def write_to_file(side1, side2, file_name='outfile.csv', delimiter=', ', print_header=False, mode='a'):
    # create a file to write to:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(dir_path, file_name)
    out_file = open(file_name, mode)
    
    # print a header if the client requests one:
    if print_header:
        print(
            'side1', 
            'side2',
            'hypotenuse',
            'area',
            'perimeter',
            sep=delimiter,
            file=out_file
        )
    # print the calculations to a file:
    print(
        side1, 
        side2,
        get_hypotenuse(side1, side2),
        get_area(side1, side2),
        get_perimeter(side1, side2),
        sep=delimiter,
        file=out_file
    )