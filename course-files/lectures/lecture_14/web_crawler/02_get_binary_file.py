from urllib.request import urlopen
import helpers


file_name = 'kitten.jpg'
url = 'https://kittenrescue.org/wp-content/uploads/2017/03/KittenRescue_KittenCareHandbook.jpg'

# 1. get it from the internet
results = urlopen(url).read()

# 2. print it to the screen
print(results)

# 3. write it to a file
# create a file path that will write to results/google.html:
file_path = helpers.get_file_path(file_name, subdirectory='results')
f = open(file_path, 'wb')
f.write(results)
f.close()