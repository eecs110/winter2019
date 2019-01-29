# a common programming pattern is to also see the for loop used
# in conjunction with the range function. This file is just for
# reference. Run the whole thing:

def print_title(text):
    print()
    print('*' * len(text))
    print(text)
    print('*' * len(text))


## Example 1
# # range function with 1 argument: 
# generates a sequence from 0 to 9 (excludes last number):
print_title('Example 1: range with 1 argument: range(10)')
for i in range(10):
    print('item', i)
## End Example 1

## Example 2
# range function with 2 arguments: 
# generates a sequence from 5 to 10 (excludes last number):
print_title('Example 2: range with 2 arguments: range(5, 10)')
for i in range(5, 10):
    print('item', i)
## End Example 2


## Example 3
print_title('Example 3: range with 3 arguments: range(2, 30, 3)')
# range function with 3 arguments: 
# generates a sequence from 2 to 30, incrementing by 3 each time (excludes last number):
for i in range(2, 30, 3):
    print('item', i)
## End Example 3
