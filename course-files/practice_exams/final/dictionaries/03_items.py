translations = {'uno': 'one', 'dos': 'two', 'tres': 'three'}

'''
Problem 3: Given the dictionary above, write a function 
that takes the translations dictionary as an argument and 
does not return anything. The function should print the 
following output to the screen:

The English translation of "uno" is "one"
The English translation of "dos" is "two"
The English translation of "tres" is "three"
'''

# option 1:
print('\nOption 1...')
for key in translations:
    print('The English translation of "' + key + '" is "' + translations[key] + '"')

# option 2:
print('\nOption 2...')
for key in translations:
    print('The English translation of "{0}" is "{1}"'.format(
        key, translations[key]
    ))

# option 3:
print('\nOption 3...')
for item in translations.items():
    print('The English translation of "{0}" is "{1}"'.format(
        item[0], item[1]
    ))

# option 4:
print('\nOption 4...')
for item in translations.items():
    print('The English translation of "{0}" is "{1}"'.format(*item))
