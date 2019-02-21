def get_file_path(path):
    import sys
    import os
    dir_path = os.path.dirname(sys.argv[0])
    return os.path.join(dir_path, path)