from urllib.request import urlopen
import helpers

# 1. get it from the internet
results = urlopen('http://www.google.com').read().decode('utf-8', 'ignore')

# 2. print it to the screen
print(results)


# 3. write it to a file
# create a file path that will write to results/google.html:
file_path = helpers.get_file_path('google.html', subdirectory='results')
f = open(file_path, 'w')
f.write(results)
f.close()