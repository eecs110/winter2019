my_string = 'hello world! How are you today?'
my_list = ['red', 'pink', 'purple', 'orange', 'teal', 'blue']


# 1. Splitting strings:
result = my_string.split('!')
print(result)

# Joining lists by a string character or characters:
print('before join:', my_list)
result = ' || '.join(my_list)
print('after join:', result)

# Detecting the length of a string:
print('The length of the string is:', len(my_string))

# Indexing a string:
print('The first character of the string is:', my_string[0])
print('The last character of the string is:', my_string[-1])


# Slicing a string:
print('The first 10 characters of the string are:', my_string[0:10])
