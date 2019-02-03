def sum(num1, num2):
    return num1 + num2

## FIXED VERSION
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

## BROKEN VERSION
# a = input('Enter the first number: ')
# b = input('Enter the second number: ')
print('The sum is: ', sum(a, b))