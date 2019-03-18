import wikipedia

term = input('What do you want to search for? ')
results = wikipedia.search(term)

print('\nI found the following items for you. What would you like to do?\n')
counter = 1
for item in results:
    print(counter, item, sep='. ')
    counter += 1