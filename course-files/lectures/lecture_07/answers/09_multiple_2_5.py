# Challenge: write a program, using a for loop, to only print numbers
# that are a multiple of 2 or 5:
numbers = [65, 1800, 12, 20, 1963, 5000, 260, 0, 40, 953, 775, 67, 33]
for num in numbers:
    if num % 5 == 0 or num % 2 == 0:
        print(num, 'is a multiple of 2 or 5.')