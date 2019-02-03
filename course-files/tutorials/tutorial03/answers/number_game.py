import random
secret_number = random.randint(1, 100)
user_guess = None

def display_secret_number(secret_number):
    message = '# [for debugging purposes] The secret number is ' + str(secret_number) + ' #'
    print()
    print('#' * len(message))
    print(message)
    print('#' * len(message))

display_secret_number(secret_number)

number_of_guesses = 0
while True:
    number_of_guesses += 1
    user_guess = input('\nGuess a number between 1 and 100 (Q to quit): ')
    if user_guess.upper() == 'Q':
        break
    # handle the case where user enters garbage:

    user_guess = int(user_guess)

    # check if too low, too high, or just right:
    if user_guess > secret_number:
        print('\n   * Your guess is too high')
    elif user_guess < secret_number:
        print('\n   * Your guess is too low')
    else:
        print('\n   * You win! It took you', number_of_guesses, 'tries to win.\n')
        break
    
