import os
import sys

def get_file_path(path, subdirectory=None):
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, path)
    else:
        return os.path.join(dir_path, path)