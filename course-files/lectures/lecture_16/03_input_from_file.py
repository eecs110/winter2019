from urllib.request import urlopen
import helpers


# From a local file:
file_path = helpers.get_file_path('sample_file.txt', subdirectory='sample_files')
f = open(file_path, 'r')
# output it to the screen:
for line in f:
    print(line)

# From a remote file:
results = urlopen('http://www.google.com').read().decode('utf-8', 'ignore')

# 2. print it to the screen
print(results)