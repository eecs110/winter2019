translations = {'uno': 'one', 'dos': 'two', 'tres': 'three'}

'''
Problem:
Given the dictionary above, write a program to print 
each Spanish word (the key) to the screen. The output 
should look like this:

uno
dos
tres
'''

# option 1:
for key in translations:
    print(key)

# option 2:
for key in translations.keys():
    print(key)