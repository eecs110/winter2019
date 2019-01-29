message = 'this is a test'
# Challenge: replace all of the spaces with asteriks using a 
# for loop and a continue statement

for letter in message:
    if letter == ' ':
        print('*')
        continue
    print(letter)


# note: an if/else statement would have worked just as well:
for letter in message:
    if letter == ' ':
        print('*')
    else:
        print(letter)
    