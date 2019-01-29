# Just an example of how some of the functions in the 
# random module work:

import random
def print_title(text):
    print()
    print('*' * len(text))
    print(text)
    print('*' * len(text))

print_title('random.randint(a, b): Picks a random integer between a and b (including endpoints)')
num1 = random.randint(30, 50)
num2 = random.randint(30, 50)
num3 = random.randint(30, 50)
print(num1, num2, num3)

print_title('random.uniform(a, b): Picks a random float between a and b (including endpoints)')
num4 = random.uniform(50, 400)
num5 = random.uniform(50, 400)
num6 = random.uniform(50, 400)
print(num4, num5, num6)

print_title("random.choice(['a', 'b', 'c', 'd', 'e']): Picks a random element from the list")
letters = ['a', 'b', 'c', 'd', 'e']
letter1 = random.choice(letters)
letter2 = random.choice(letters)
letter3 = random.choice(letters)
print(letter1, letter2, letter3)