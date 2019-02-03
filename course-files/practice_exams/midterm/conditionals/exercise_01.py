'''
Write a function called even_or_odd that takes 1 positional parameter —  
an int called num — and returns a string that says either “even” or “odd”
Prove that your function works by printing the results of several 
function calls to the screen.
'''

def even_or_odd(num):
    # if you divide by 2 and the remained is 0, it's even
    if num % 2 == 0:
        return 'even'
    # otherwise, it's odd
    else:
        return 'odd'

print('5:', even_or_odd(5))
print('18:', even_or_odd(18))
print('125:', even_or_odd(125))