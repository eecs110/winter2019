my_list = [ 
'billy', False, { 'first_name': 'Joan', 'last_name': 'Galini' } 
]
a = my_list.pop()
b = my_list.pop(0)
my_list += [3, 5]
my_list.append(['red',  'blue',  'pink'])
my_list[0] = 1000
print(a)
print(b)
print(my_list)
print(my_list[-1])