d = []
e = 1
f = None

if d and e:
    print('d and e evaluated to True')
else:
    print('d and e evaluated to False')

if d or e:
    print('d or e evaluated to True')
else:
    print('d or e evaluated to False')

if d and f:
    print('d and d evaluated to True')
else:
    print('d and f evaluated to False')

if not (d and f):
    print('not (d and f) evaluated to True')
else:
    print('not (d and f) evaluated to False')