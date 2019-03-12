my_list = []
a = [1, 2, 3]
b = [4, 5, 6]
my_list.append(a)
print(my_list)
my_list += b
print(my_list)

# How would I fix this code so that the output looked 
# like this...[1, 2, 3, 4, 5, 6]

# option 1:
print('fixed...')
my_list = []
my_list += a + b
print(my_list)
