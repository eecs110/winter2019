import sys
import os

def get_file_path(file_name):
    dir_path = os.path.dirname(sys.argv[0])
    return os.path.join(dir_path, file_name)