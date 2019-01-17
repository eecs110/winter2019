'''
Below is code to write a greeting to Varun and Grace. The code
prints out a line break on the first line, 20 asteriks on the
second line, a greeting on the third line, and 20 asteriks on the
fourth line.

Your boss just called, and she needs you to print individual messages 
for every student at Northwestern -- and you only have a half hour! 

Not to worry! Functions can help! Please complete the following
tasks:

1. Modify the rows of asteriks so that the length of the asteriks
is exactly the length of the greeting printed in between them. 
For instance, instead of 
********************
Hello Varun!
********************

it should say:

************
Hello Varun!
************

2. Next, create a function, print_greeting(), that has one positional parameter
called name.  This function should print the greeting, but instead of hard coding
the name, the name should be passed in as a parameter.

When you're done, refactor your code so that you call your print_greeting() function
twice (with different names) in order to print the full greeting (using arguments).

3. If you did that, add a keyword parameter to your print_greeting() function that 
specifies which character you can use for your banner. Asterik can be the default, but
any character should be possible.

************************************************************************************
'''


# Begin code:
print('*' * 20)
print('Hello Varun!')
print('*' * 20)
print('\n')

print('*' * 20)
print('Hello Grace!')
print('*' * 20)
print('\n')


# list goes on an on...
students_at_northwestern = [
    'Varun', 'Grace', 'Leigh', 'Brooke', 'Anel', 'Erick'
]