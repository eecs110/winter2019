# Note: both a and b evaluate to true because they're not 0, False, or None
a = [3, 5]
b = 22
c = 0
d = []
e = 1
f = None

if a and b:
    print('a and b evaluated to True')
else:
    print('a and b evaluated to False')

if a and c:
    print('a and c evaluated to True')
else:
    print('a and c evaluated to False')

if a or c:
    print('a or c evaluated to True')
else:
    print('a or c evaluated to False')