translations = {'uno': 'one', 'dos': 'two', 'tres': 'three'}

'''
Problem:
Given the dictionary above, write a program to print 
each English word (the key) to the screen. The output 
should look like this:

one
two
three
'''

# option 1:
for key in translations:
    print(translations[key])

# option 2:
for val in translations.values():
    print(val)