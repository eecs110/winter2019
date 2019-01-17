####################################################################
## Example 1: function with no arguments and no return value
def say_hello():
    print('Hello there!')
    print('\n')

say_hello()
say_hello()
say_hello()
## End Example 1
####################################################################



####################################################################
## Example 2: function with one positional parameter, which allows
# the message to be changed everytime the function is called.
def say_hello_1(name):
    print('Hello ' + name + '!')
    print('How are you this morning?')
    print('\n')


say_hello_1('Varun')
say_hello_1('Grace')
say_hello_1('Tamara')
# In this example, one positional argument is required. If you 
# don't pass the function 1 argument, it will throw an error.
# 
# say_hello_1()    # throws a runtime error
## End Example 2
####################################################################



####################################################################
## Example 3: function with two positional parameters:
#   - one for the name
#   - one for the time of day
#  Parameters make functions more flexible
def say_hello_2(name, time_of_day):
    print('Hello ' + name + '!')
    print('How are you this ' + time_of_day + '?')
    print('\n')


say_hello_2('Varun', 'morning')
say_hello_2('Grace', 'evening')
say_hello_2('Tamara', 'afternoon')
# In this example, one positional argument is required. If you 
# don't pass the function 1 argument, it will throw an error.
# 
# say_hello_2('Varun')    # throws a runtime error
## End Example 3
####################################################################


####################################################################
## Example 4: function with one keyword (optional) parameter
def say_hello_3(time_of_day='morning'):
    print('How are you this ' + time_of_day + '?')
    print('\n')


say_hello_3(time_of_day='morning')
say_hello_3(time_of_day='evening')
say_hello_3(time_of_day='afternoon')
say_hello_3('morning')  # also valid (but not recommended)
say_hello_3('evening')  # also valid (but not recommended)
say_hello_3('afternoon')  # also valid (but not recommended)
# In this example, because the keyword argument is option, if you
# don't include it, it takes the default:
say_hello_3()    # takes the default
## End Example 4
####################################################################


####################################################################
## Example 5: function with one positional parameter and one 
#  keyword (optional) parameter
def say_hello_4(name, time_of_day='morning'):
    print('Hello ' + name + '!')
    print('How are you this ' + time_of_day + '?')
    print('\n')


say_hello_4('Varun', time_of_day='morning')
say_hello_4('Grace', time_of_day='evening')
say_hello_4('Tamara', time_of_day='afternoon')
say_hello_4('Varun', 'morning')  # also valid (but not recommended)
say_hello_4('Grace', 'evening')  # also valid (but not recommended)
say_hello_4('Tamara', 'afternoon')  # also valid (but not recommended)
say_hello_4('Varun')
## End Example 5
####################################################################

